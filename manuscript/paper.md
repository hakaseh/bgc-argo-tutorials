---
title: 'bgc-argo-tutorials: A practical guide to biogeochemical Argo data analysis'
tags: 
  - BGC-Argo
  - Jupyter Notebook
  - Python
  - Oceanography
  - Marine ecosystems

authors:
  - name: Haruto Fujishima
    orcid: 0009-0000-3510-1133
    equal-contrib: true
    affiliation: 1
  - name: Hakase Hayashida
    orcid: 0000-0002-6349-4947
    equal-contrib: true
    affiliation: 2
    corresponding: true

affiliations:
  - name: Department of Geophysics, Graduate School of Science, Tohoku University, Sendai, Japan
    index: 1
  - name: Application Laboratory, Japan Agency for Marine-Earth Science and Technology, Yokohama, Japan
    index: 2

date: 16 April 2026
bibliography: paper.bib
---

# Summary

Biogeochemical Argo (BGC-Argo) is an ocean observing system for monitoring the health of marine ecosystems by a global array of autonomous profiling floats that routinely measure biogeochemical oceanographic properties in the upper 2,000 m of the water column every 10 days or so [@claustre2020]. By 2030, the global BGC-Argo community aims to cover the global ocean with 1,000 floats equipped with sensors that can measure up to six key variables: chlorophyll-a, pH, oxygen, nitrate, irradiance, and suspended particles [@thierry2025]. The collected profiles are made publicly available in the netCDF format within a day or so, and can be used for scientific analysis and operational purposes.

Here we introduce **bgc-argo-tutorials**, which provides a step-by-step guide on the analysis of BGC-Argo data using Python and Jupyter Notebook. This learning module is designed for graduate students and early-career researchers of Oceanography [e.g., Early Career Ocean Professionals or ECOPs\; @li_early_2025] ready to dive into BGC-Argo data analysis for their research projects. A basic knowledge on the Argo program [@wong2020] and BGC-Argo [@bittig2019] is a prerequisite. **bgc-argo-tutorials** provides lessons on how to search, identify, download, and post-process the profiles for conducting time-series analysis. The end product of **bgc-argo-tutorials** can be used for understanding the spatial and temporal variability of ocean dynamics and biogeochemistry, evaluating the performance of numerical model simulations and other data products, and improving ocean biogeochemical prediction. **bgc-argo-tutorials** aims to help expand the end users of the growing BGC-Argo data in Japan and beyond.

# Statement of need

While the BGC-Argo database is an invaluable resource, the native formatting of the NetCDF files presents a steep learning curve for new users. Direct utilization of the raw datasets is computationally cumbersome due to non-standard data typing, such as the use of string arrays for Quality Control (QC) flags instead of easily maskable integers. Furthermore, because the vertical sampling depths vary irregularly across individual profiles, the data must be interpolated onto a standardized depth grid to enable continuous 2D visualizations and direct comparisons with gridded model and other data products. **bgc-argo-tutorials** addresses these bottlenecks by providing working examples and functions for the necessary post-processing of the data. 

The scope and approach of **bgc-argo-tutorials** are structurally different from other existing softwares, learning modules, and data products related to BGC-Argo, because it requires users to understand the source code for each function developed within [cf. @maze2020], it focuses specifically on BGC-Argo and is targeted at users with basic knowledge on BGC-Argo [cf. @gonzalez-santana_argo_2024], and it gives access to post-processed data on a near-real-time basis [cf. @johnson2023]. The idea for **bgc-argo-tutorials** was conceived when the corresponding author started using the BGC-Argo data for the first time and experienced the issues mentioned above [@hayashida2025]. The author also noticed the relatively low use cases by the Japanese researchers (out of the 849 BGC-Argo papers published, only 24 papers are led by authors with the Japanese surnames; https://argo.ucsd.edu/outreach/publications/biogeochemical-argo-bibliography/ as of February 2, 2026). To address this regional issue, we provide support for **bgc-argo-tutorials** in Japanese and organize on-site tutorial sessions in the near future.

Earlier versions of **bgc-argo-tutorials** were presented at the Japan Geoscience Union Meeting 2025 in Chiba and the Oceanographic Society of Japan Fall Meeting 2025 in Hokkaido. A hands-on workshop on BGC-Argo data analysis using **bgc-argo-tutorials** will be held as a side event of the OneArgo international workshop in Miyagi on June 2, 2026. An earlier version of **bgc-argo-tutorials** has been used for the assessment of seasonal ocean prediction of chlorophyll-a and nitrate in the equatorial Pacific by a global climate model [@doi2026].

# Acknowledgements

BGC-Argo data are made freely available through the two Global Data Assembly Centres [GDACs\; @gdac]. We thank Hidehiro Fujio for computational assistance and Pete Strutton, Clara Vives, Kanako Sato, Yoshimi Kawai for insightful discussion on BGC-Argo floats and feedback on earlier versions of **bgc-argo-tutorials**. This work was supported by JSPS KAKENHI Grant Number JP24H02226 and the Nakajima Foundation.

# References


