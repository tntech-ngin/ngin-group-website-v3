---
title: "N-DISE: NDN for Data Intensive Science Experiments"
date: 2020-09-01
tags:
  - "NDN"
  - "High Energy Physics"
  - "CERN"
  - "LHC"
  - "NSF"
summary: "Deploying the first prototype production-ready NDN-based petascale data distribution system for high-energy physics."
external_link: "https://ndise.net"
funder: "NSF CC* #2019012"
amount: "$1,025,000"
featured: true
collaborators:
  - "Northeastern University"
  - "Caltech"
  - "UCLA"
---

The Large Hadron Collider (LHC) at CERN generates petabytes of collision data annually that must be distributed to hundreds of physics institutes worldwide for analysis. Current TCP/IP-based systems require complex software-defined networking overlays and dedicated infrastructure to manage this scale.

**N-DISE** (NDN for Data Intensive Science Experiments) aims to deploy and commission the first prototype production-ready Named Data Networking (NDN)-based petascale data distribution, caching, access, and analysis system, with LHC high-energy physics as the primary target use case.

The project addresses:
- **Location-transparent data access** — physicists request data by dataset name, not server location
- **In-network caching** — frequently accessed datasets are cached closer to consumers automatically
- **Integration with XRootD** — the standard HEP data access protocol, extended with an NDN plugin
- **Wide-area testbed** — a production-grade national testbed spanning CERN, Caltech, Nebraska, and TNTech

N-DISE has produced the first NDN-based XRootD plugin, presented at CHEP 2023 and EPJ Web of Conferences, and a wide-area testbed now available to the HEP community.

**Funding:** NSF CC* Integration-Large #2019012 ($1,025,000, TNTech share: $115,500)

**Code:** [github.com/neu-yehlab/n-dise](https://github.com/neu-yehlab/n-dise)

**Team:** Susmit Shannigrahi (Co-PI/TNTech), Edmund Yeh (PI/Northeastern), Harvey Newman (Caltech), Lixia Zhang (UCLA), Davide Pesavento, Sankalpa Timilsina
