Lifecycle Dynamics of Aadhaar Enrolment and Updates
A State-Level Comparative Analysis Using Socio-Demographic Indicators in India

Author: Ritesh Verma
Hackathon: UIDAI Data-Driven Innovation Hackathon 2026
Date: January 2026

Project Overview

Aadhaar is a foundational digital identity system supporting governance, welfare delivery, and service access across India. While enrolment and update activities occur continuously, their intensity and nature vary significantly across states due to demographic, economic, and mobility-related factors.

This project analyses Aadhaar enrolment, demographic updates, and biometric updates at the state level, contextualised using population structure, literacy, migration, and economic indicators. The objective is to move beyond raw counts and uncover systemic patterns that explain why Aadhaar interaction behaviour differs across regions.

The analysis is fully reproducible and based on aggregated, anonymised UIDAI datasets combined with publicly available census and economic data.

Key Objectives

Understand how age structure influences Aadhaar enrolment and update activity

Examine the role of migration in driving demographic updates

Analyse whether literacy and economic development affect Aadhaar engagement

Identify state-level behavioural typologies based on update patterns

Simulate future scenarios to support data-driven policy planning

Datasets Used
1. UIDAI Datasets (Aggregated & Anonymised)

Aadhaar Enrolment Dataset

Age groups: 0–5, 5–17, 18+

Aadhaar Demographic Update Dataset

Age groups: 5–17, 17+

Aadhaar Biometric Update Dataset

Age groups: 5–17, 17+

All UIDAI datasets are aggregated at state/UT level and contain no personal data.

2. Secondary Datasets
Dataset	Source
Population & Density (2011)	Census of India
Literacy Rate (2011)	Census of India
Migration Indicators	Census of India
Age Structure (18+ Share)	Census of India
Per Capita GSDP (Latest)	MOSPI / State Economic Surveys

Methodology Overview
1. Data Preparation

Standardised state names across all datasets

Removed non-state administrative entries

Aggregated UIDAI data from district/pincode to state level

Normalised update counts per million population

2. Dataset Integration

All datasets were merged into a single state-level analytical table containing:

Enrolment counts

Demographic & biometric updates

Population, literacy, migration, GSDP

Share of population aged 18+

Key Findings

Migration is a strong driver of demographic updates

Literacy improves sustained engagement with Aadhaar

Economic growth increases update activity rather than reducing it

Some high-income states face greater update pressure than poorer states

Proactive policy design can prevent system overload

Limitations

State-level aggregation masks district-level variation

Migration indicators are census-based and may lag real-time movement

Causal relationships are inferred, not experimentally proven

Reproducibility

All analysis scripts are included in this repository.
Running the scripts in sequence reproduces the dataset, visualisations, and analytical outputs used in the paper.

License & Data Use

UIDAI data used is aggregated and anonymised

Census and economic data are publicly available

This project is for research and policy analysis purposes only

Contact

Ritesh Verma
Hackathon Participant – UIDAI Data Innovation
vritesh328@gmail.com
