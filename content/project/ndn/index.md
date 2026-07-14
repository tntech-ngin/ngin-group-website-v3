---
title: "Named Data Networking (NDN)"
date: 2013-01-01
tags:
  - "NDN"
  - "Future Internet"
  - "Network Architecture"
  - "NSF"
summary: "A Future Internet Architecture that shifts the fundamental network primitive from where to what."
external_link: "https://named-data.net"
collaborators:
  - "CERN"
  - "Caltech"
  - "LBNL"
  - "Clemson"
---

The current Internet was designed to connect computers — hosts — and everything is addressed by location (IP address). As the Internet has evolved into a content delivery system, this host-centric model creates inefficiencies: the same popular content is downloaded repeatedly from origin servers, security is bolted on rather than built in, and mobility requires complex workarounds.

**Named Data Networking (NDN)** is a Future Internet Architecture that shifts the fundamental network primitive from *where* to *what*. Instead of "send a packet to 192.168.1.1," NDN consumers say "give me /climate/noaa/2024/temperature-data." The network itself can cache, aggregate, and route based on content names.

Key properties:
- **In-network caching** — routers cache content by name; the second requester gets it from the nearest cache
- **Content-centric security** — data is signed by the producer, verified by the consumer; trust follows content, not connection
- **Mobility** — consumers can move freely; interest packets find content regardless of where producer or consumer are
- **Multicast by default** — multiple consumers requesting the same name receive a single copy

The NGIN Lab has contributed to NDN since 2013, including core contributions to NFD (the NDN Forwarding Daemon), ndn-cxx, NDN-atmos (climate data), and SANDIE (HEP data). NDN software from this lab has been deployed at CERN, Caltech, LBNL, Clemson, and CSU.

**Code:** [github.com/named-data](https://github.com/named-data) | [github.com/tntech-ngin](https://github.com/tntech-ngin)
