#!/usr/bin/env python3
"""Convert bibliography/susmit_cv.bib into data/publications.yaml for Hugo.

Usage: scripts/.venv/bin/python scripts/build_publications.py
Re-run any time bibliography/susmit_cv.bib changes (the Makefile does this
automatically before `make serve` / `make build`).
"""
import re
import sys
from collections import OrderedDict
from pathlib import Path

import bibtexparser
import yaml
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import author, convert_to_unicode

ROOT = Path(__file__).resolve().parent.parent
BIB_PATH = ROOT / "bibliography" / "susmit_cv.bib"
OUT_PATH = ROOT / "data" / "publications.yaml"

VENUE_FIELDS_BY_TYPE = {
    "article": ["journal"],
    "inproceedings": ["booktitle"],
    "conference": ["booktitle"],
    "incollection": ["booktitle"],
    "phdthesis": ["school"],
    "mastersthesis": ["school"],
    "techreport": ["institution"],
    "book": ["publisher"],
}
FALLBACK_VENUE_FIELDS = ["journal", "booktitle", "organization", "publisher", "howpublished", "institution", "school"]


def clean_text(value):
    if not value:
        return ""
    value = value.replace("--", "–")
    value = re.sub(r"\s+", " ", value).strip()
    value = value.strip("{}")
    return value


def format_author(raw):
    raw = clean_text(raw)
    if "," in raw:
        last, _, first = raw.partition(",")
        return f"{first.strip()} {last.strip()}".strip()
    return raw


def venue_for(record):
    entry_type = record.get("ENTRYTYPE", "").lower()
    for field in VENUE_FIELDS_BY_TYPE.get(entry_type, []):
        if record.get(field):
            return clean_text(record[field])
    for field in FALLBACK_VENUE_FIELDS:
        if record.get(field):
            return clean_text(record[field])
    return ""


def link_for(record):
    if record.get("url"):
        return clean_text(record["url"])
    if record.get("doi"):
        return f"https://doi.org/{clean_text(record['doi'])}"
    return ""


def customizations(record):
    record = convert_to_unicode(record)
    record = author(record)
    return record


def load_entries():
    parser = BibTexParser(common_strings=True)
    parser.customization = customizations
    parser.ignore_nonstandard_types = False
    with open(BIB_PATH, encoding="utf-8") as f:
        db = bibtexparser.load(f, parser=parser)
    return db.entries


def main():
    if not BIB_PATH.exists():
        print(f"error: {BIB_PATH} not found", file=sys.stderr)
        sys.exit(1)

    entries = load_entries()

    seen_keys = {}
    for e in entries:
        key = e.get("ID", "")
        seen_keys[key] = seen_keys.get(key, 0) + 1
    dupes = [k for k, count in seen_keys.items() if count > 1]
    if dupes:
        print(f"warning: duplicate citekeys in {BIB_PATH.name}, all copies kept: {', '.join(dupes)}", file=sys.stderr)

    by_year = OrderedDict()
    for record in entries:
        year_raw = clean_text(record.get("year", ""))
        year = int(year_raw) if year_raw.isdigit() else None
        authors = [format_author(a) for a in record.get("author", [])]
        pub = {
            "key": record.get("ID", ""),
            "title": clean_text(record.get("title", "")),
            "authors": authors,
            "venue": venue_for(record),
            "year": year,
            "link": link_for(record),
        }
        by_year.setdefault(year, []).append(pub)

    year_groups = [
        {"year": year, "entries": pubs}
        for year, pubs in sorted(by_year.items(), key=lambda kv: (kv[0] is None, -(kv[0] or 0)))
    ]

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        yaml.dump(year_groups, f, allow_unicode=True, sort_keys=False, width=1000)

    total = sum(len(g["entries"]) for g in year_groups)
    print(f"wrote {total} publications ({len(year_groups)} year groups) to {OUT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
