---
title: "hipFT: High-Performance Error-Free File Transfer"
date: 2020-08-01
tags:
  - "File Transfer"
  - "Big Science"
  - "Network Protocols"
  - "NSF"
summary: "End-to-end integrity verification for large-scale scientific data transfers over Science DMZ networks."
external_link: "https://hipft.net"
funder: "NSF CC* #2019163"
amount: "$470,431"
collaborators:
  - "Colorado State University"
---

Large-scale scientific data transfers over the Internet are routinely corrupted by undetected bit errors — a problem invisible to TCP/IP, which provides no end-to-end data integrity guarantees beyond the link layer. For genomics, climate, and high-energy physics datasets, even rare corruption events can silently invalidate months of computation.

**hipFT** (High-Performance File Transfer) enables users to transfer large files with confidence that data will be accurately and efficiently copied across the network. Key features:

- **End-to-end integrity verification** beyond what TCP provides
- **Optimized for high-bandwidth, high-latency Science DMZ networks**
- **Compatible with existing storage and workflow infrastructure**
- Demonstrates that significant undetected error rates exist on production Internet paths

This project is a collaboration with Craig Partridge and Christos Papadopoulos at Colorado State University.

**Funding:** NSF CC* Integration Small #2019163 — *Error Free File Transfer for Big Science* ($470,431, TNTech share: $162,416)

**Code:** [hipft.net](https://hipft.net)

**Team:** Susmit Shannigrahi (Co-PI), Sepideh Abdollah, Craig Partridge (Co-PI, CSU), Christos Papadopoulos (CSU)
