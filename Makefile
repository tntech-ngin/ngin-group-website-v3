VENV := scripts/.venv
PYTHON := $(VENV)/bin/python

.PHONY: venv publications serve build

venv:
	@test -d $(VENV) || python3 -m venv $(VENV)
	@$(PYTHON) -m pip install --quiet -r scripts/requirements.txt

publications: venv
	@$(PYTHON) scripts/build_publications.py

serve: publications
	hugo server -D

build: publications
	hugo --gc --cleanDestinationDir
