<h1 align="center">Lifecycle Dynamics of Aadhaar Enrolment and Updates</h1>
<h3 align="center">
A State-Level Comparative Analysis Using Socio-Demographic Indicators in India
</h3>

<p align="center">
<strong>Author:</strong> Ritesh Verma<br>
<strong>Hackathon:</strong> UIDAI Data-Driven Innovation Hackathon 2026<br>
<strong>Date:</strong> January 2026
</p>

<hr>

<h2>Project Overview</h2>

<p>
Aadhaar is a foundational digital identity system supporting governance, welfare delivery,
and service access across India. While enrolment and update activities occur continuously,
their intensity and nature vary significantly across states due to demographic, economic,
and mobility-related factors.
</p>

<p>
This project analyses Aadhaar enrolment, demographic updates, and biometric updates at
the state level, contextualised using population structure, literacy, migration, and
economic indicators. The objective is to move beyond raw counts and uncover systemic
patterns that explain why Aadhaar interaction behaviour differs across regions.
</p>

<p>
The analysis is fully reproducible and based on aggregated, anonymised UIDAI datasets
combined with publicly available census and economic data.
</p>

<hr>

<h2>Key Objectives</h2>

<ul>
  <li>Understand how age structure influences Aadhaar enrolment and update activity</li>
  <li>Examine the role of migration in driving demographic updates</li>
  <li>Analyse whether literacy and economic development affect Aadhaar engagement</li>
  <li>Identify state-level behavioural typologies based on update patterns</li>
  <li>Simulate future scenarios to support data-driven policy planning</li>
</ul>

<hr>

<h2>Datasets Used</h2>

<h3>1. UIDAI Datasets <em>(Aggregated &amp; Anonymised)</em></h3>

<ul>
  <li>
    <strong>Aadhaar Enrolment Dataset</strong><br>
    Age groups: 0–5, 5–17, 18+
  </li>
  <li>
    <strong>Aadhaar Demographic Update Dataset</strong><br>
    Age groups: 5–17, 17+
  </li>
  <li>
    <strong>Aadhaar Biometric Update Dataset</strong><br>
    Age groups: 5–17, 17+
  </li>
</ul>

<p>
All UIDAI datasets are aggregated at state/UT level and contain no personal data.
</p>

<h3>2. Secondary Datasets</h3>

<table>
  <thead>
    <tr>
      <th align="left">Dataset</th>
      <th align="left">Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Population &amp; Density (2011)</td>
      <td>Census of India</td>
    </tr>
    <tr>
      <td>Literacy Rate (2011)</td>
      <td>Census of India</td>
    </tr>
    <tr>
      <td>Migration Indicators</td>
      <td>Census of India</td>
    </tr>
    <tr>
      <td>Age Structure (18+ Share)</td>
      <td>Census of India</td>
    </tr>
    <tr>
      <td>Per Capita GSDP (Latest)</td>
      <td>MOSPI / State Economic Surveys</td>
    </tr>
  </tbody>
</table>

<hr>

<h2>Methodology Overview</h2>

<h3>1. Data Preparation</h3>

<ul>
  <li>Standardised state names across all datasets</li>
  <li>Removed non-state administrative entries</li>
  <li>Aggregated UIDAI data from district/pincode to state level</li>
  <li>Normalised update counts per million population</li>
</ul>

<h3>2. Dataset Integration</h3>

<p>
All datasets were merged into a single state-level analytical table containing:
</p>

<ul>
  <li>Enrolment counts</li>
  <li>Demographic &amp; biometric updates</li>
  <li>Population, literacy, migration, GSDP</li>
  <li>Share of population aged 18+</li>
</ul>

<hr>

<h2>Key Findings</h2>

<ul>
  <li>Migration is a strong driver of demographic updates</li>
  <li>Literacy improves sustained engagement with Aadhaar</li>
  <li>Economic growth increases update activity rather than reducing it</li>
  <li>Some high-income states face greater update pressure than poorer states</li>
  <li>Proactive policy design can prevent system overload</li>
</ul>

<hr>

<h2>Limitations</h2>

<ul>
  <li>State-level aggregation masks district-level variation</li>
  <li>Migration indicators are census-based and may lag real-time movement</li>
  <li>Causal relationships are inferred, not experimentally proven</li>
</ul>

<hr>

<h2>Reproducibility</h2>

<p>
All analysis scripts are included in this repository. Running the scripts in sequence
reproduces the dataset, visualisations, and analytical outputs used in the paper.
</p>

<hr>

<h2>License &amp; Data Use</h2>

<ul>
  <li>UIDAI data used is aggregated and anonymised</li>
  <li>Census and economic data are publicly available</li>
  <li>This project is for research and policy analysis purposes only</li>
</ul>

<hr>

<h2>Contact</h2>

<p>
<strong>Ritesh Verma</strong><br>
Hackathon Participant – UIDAI Data Innovation<br>
📧 <a href="mailto:vritesh328@gmail.com">vritesh328@gmail.com</a>
</p>
