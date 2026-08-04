---
title: "Another Big Win: Building an Autonomous Water Control System for Floodplain Nutrient Retention"
date: 2026-08-04
tag: "grant"
summary: "An EPA-funded, machine-learning-based water control system that decides on its own when to hold and release floodplain water to maximize nutrient retention."
---

As part of our EPA-funded project on water quality in the Gulf of America watershed, we're building a **smart, machine-learning-based autonomous water control system** for floodplain wetlands.

Water control structures like flashboard risers and screw gates are the standard tool for managing how long flood water stays on a floodplain, which strongly affects how much nitrogen and phosphorus it retains. Today, operating them means someone physically visiting the site, visually assessing conditions, and manually adjusting the gate. Our system automates that decision loop end to end.

![System diagram: a LoRa sensor mesh across a wetland easement feeds an AI/ML forecasting and predictive control loop that actuates a smart flashboard riser gate](/project/epa-982000/system-diagram.png)

Low-power sensors spread across the wetland easement report hydrology, nutrient concentration, vegetation, soil, and weather data over a LoRa mesh network back to an on-site Jetson Nano, which continuously updates a machine learning model forecasting soil moisture and floodplain conditions. When conditions are right, the system self-operates an actuator-driven flap gate on a smart flashboard riser, deciding both the timing and volume of release to maximize nitrogen and phosphorus retention, with no one needing to be on site.

Read more on the [project page](/project/epa-982000/).
