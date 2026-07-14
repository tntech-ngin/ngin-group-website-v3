---
title: "Hydra: Distributed Repository over NDN"
date: 2021-09-01
tags:
  - "NDN"
  - "Big Science"
  - "Distributed Systems"
  - "Genomics"
  - "NSF"
summary: "A framework for building a loose federation of scientific data repositories over Named Data Networking."
external_link: "http://www.hydra-repo.io"
funder: "NSF CC* #2126148"
amount: "$997,221"
featured: true
collaborators:
  - "UCLA"
  - "FIU"
  - "Clemson University"
---

Big science communities — genomics, climate, high-energy physics, weather sensing — store data across centralized and ad-hoc repositories, each with different publication and access standards. Researchers waste enormous time locating, authenticating, and transferring data across incompatible systems.

**Hydra** is a framework for building a loose federation of repositories over Named Data Networking (NDN). It provides:

- **Automated replication** across federated nodes with configurable policies
- **Built-in security** using NDN's content-centric trust model
- **Location-transparent data access** — consumers request data by name, not by server address
- **Multi-objective optimization** for replica placement (GNSGA, PSMOA algorithms)

Hydra has been deployed and tested with genomics workflows in collaboration with Clemson University, demonstrating petascale data management across geographically distributed research sites. It has been presented at BioIT World, NSF CC* PI Meeting, KNIT, and FABRIC community workshops.

**Funding:** NSF CC* Integration-Large #2126148 — *Prototyping a Secure Distributed Storage Infrastructure for Accelerating Big Science* ($997,221)

**Code:** [github.com/tntech-ngin/ndn-hydra](https://github.com/tntech-ngin/ndn-hydra)

**Team:** Susmit Shannigrahi (PI), Sankalpa Timilsina, Xi Wang, Tianyuan Yu, Lixia Zhang (UCLA), Alex Afanasyev (FIU), F. Alex Feltus (Clemson)
