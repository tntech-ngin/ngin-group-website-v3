---
title: "Vehicular Network Security"
date: 2020-08-01
tags:
  - "Vehicular Networks"
  - "CAN Bus"
  - "NDN"
  - "Cybersecurity"
  - "IoT"
summary: "Securing in-vehicle CAN bus communication and vehicle-to-everything (V2X) networking using NDN's content-centric model."
collaborators:
  - "Colorado State University"
---

Modern vehicles are increasingly connected — to each other, to roadside infrastructure, and to the cloud — while running hundreds of electronic control units (ECUs) communicating over the Controller Area Network (CAN bus). This creates a large and largely unprotected attack surface: CAN bus has no built-in authentication or encryption, and a compromised ECU can issue commands to brakes, steering, and engine systems.

The NGIN Lab's vehicular security research addresses two complementary problems:

**In-vehicle security:**
- Analyzing CAN bus traffic to detect anomalous or spoofed messages
- Designing moving target defense protocols (DAVA) that randomize CAN IDs to prevent replay attacks
- Using Named Data Networking for secure in-vehicle communication with built-in content authentication

**Vehicle-to-everything (V2X) security:**
- Applying NDN's name-based security model to vehicular networking
- Designing secure mobility planes for V2X communication
- Formal security analysis of vehicular network architectures

This work is done in collaboration with Christos Papadopoulos (CSU), Fadi Mohsen, Usman Rauf, and Micah Jones.

**Code:** [github.com/tntech-ngin](https://github.com/tntech-ngin)
