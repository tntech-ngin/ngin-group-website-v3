---
title: "Innovative Solutions for Improving Water Quality in the Gulf of America Watershed"
date: 2025-07-01
tags:
  - "EPA"
  - "Water Quality"
  - "Environmental Monitoring"
  - "Machine Learning"
  - "IoT"
summary: "A machine-learning-based autonomous water control system that decides when, how much, and how long to hold water on floodplain wetlands to maximize nutrient retention."
status: "active"
funder: "EPA #982000"
amount: "$993,953"
collaborators: []
---

Floodplain hydrology is a major driver of nutrient cycling in agricultural watersheds. How long flood water stays on a floodplain strongly affects how much nitrogen and phosphorus it retains, through denitrification, biotic uptake, and sedimentation. Water control structures such as flashboard risers and screw gates are the standard tool for managing that retention, but today they require someone to physically visit the site, visually assess conditions, and manually adjust the gate, work that's slow, subjective, and hard to scale across a watershed.

This project builds a smart, machine-learning-based autonomous water control system that makes those decisions on its own: when, how much, and how long to hold water on a riparian wetland or floodplain field to maximize nitrogen and phosphorus retention. An initial model is seeded from prior nutrient-retention research in the study region (Alexander et al. 2025, Brown et al. 2025, Murdock et al., in prep), then continuously improved through real-time input from on-the-ground sensors and remote data collection covering hydrology, nutrient concentration, vegetation, soil conditions, and weather.

![System diagram: a LoRa sensor mesh across a wetland easement feeds an AI/ML forecasting and predictive control loop that actuates a smart flashboard riser gate](system-diagram.png)

In the field, low-power sensor nodes exchange data over a LoRa mesh network and report back through a cellular gateway. A Jetson Nano handles on-site ML training and decision-making, continuously updating a pre-trained model that forecasts soil moisture and floodplain conditions, feeds a predictive control loop, and watches for anomalies. When conditions are right, the system self-operates an actuator-driven flap gate on a **smart flashboard riser**, deciding both the timing and the volume of release, closing the loop between sensing, prediction, and control without anyone needing to be on site.

This complements the NGIN Lab's other low-cost environmental sensing work (see the [turbidity sensor project](/project/turbidity-sensor/)).

**Funding:** Environmental Protection Agency, Grant #982000 — *Innovative Solutions for Improving Water Quality and Strengthening Local Economies in the Gulf of America Watershed* ($993,953, 2025–)

**Team:** Susmit Shannigrahi (Co-PI)
