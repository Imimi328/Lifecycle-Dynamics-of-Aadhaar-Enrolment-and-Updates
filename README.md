<!DOCTYPE html>
<html lang="en">

<body>

<h1>Lifecycle Dynamics of Aadhaar Enrolment and Updates</h1>
<h3>A State-Level Comparative Analysis Using Socio-Demographic Indicators in India</h3>

<p><strong>Author:</strong> Ritesh Verma<br>
<strong>Date:</strong> January 2026<br>
<strong>Hackathon:</strong> UIDAI Data-Driven Innovation Hackathon 2026</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
Aadhaar is one of the world’s largest biometric digital identity systems, underpinning service delivery,
welfare distribution, and administrative governance across India. While enrolment and update activities
occur continuously, their <em>intensity, composition, and drivers vary significantly across states</em>.
</p>

...

<hr>

<h2>📂 Datasets Used</h2>

<h3>Primary Dataset (Aadhaar interaction + State Indicators)</h3>

<ul>
  <li>
    <strong>Combined Measurement Dataset:</strong>
    <a href="https://drive.google.com/file/d/1gZ0fNI8kbzAJsdLx-R9M7lpV_DYdF5s_/view?usp=sharing" target="_blank">
      Download from Google Drive
    </a>
    <p>This dataset includes:</p>
    <ul>
      <li>State-wise Aadhaar enrolment counts by age groups</li>
      <li>Demographic and biometric updates</li>
      <li>Socio-demographic indicators (literacy, population structure, migration intensity)</li>
      <li>Normalised interaction scores (per million population)</li>
    </ul>
  </li>
</ul>

<p>
You can use this file to reproduce figures, build new models, or extend the analysis.
</p>

<h3>Other Sources</h3>

<ul>
  <li><strong>UIDAI Hackathon Official Data</strong> (enrolment & update datasets)</li>
  <li><strong>Census 2011</strong> (population, literacy, migration)</li>
  <li><strong>Per-Capita GSDP</strong> (state economic indicators)</li>
</ul>

<hr>

<h2>⚙️ How to Use the Dataset</h2>

<p>
You can open the dataset in any standard analysis environment (Pandas, R, Excel). Below is an example of loading it using Python and Pandas:
</p>

<pre>
import pandas as pd

# Replace path with local path after downloading
df = pd.read_csv("combined_aadhaar_state_data.csv")

print(df.head())
</pre>

<p>
Ensure you have installed <code>pandas</code> if running locally:
</p>

<pre>
pip install pandas
</pre>

<hr>

<h2>📑 Paper & Resources</h2>

<ul>
  <li>
    <strong>Full Paper (PDF):</strong>
    <a href="https://figshare.com/ndownloader/files/60991291/preview/60991291/preview.pdf" target="_blank">
      View on Figshare
    </a>
  </li>
  <li>
    <strong>Dataset:</strong>
    <a href="https://drive.google.com/file/d/1gZ0fNI8kbzAJsdLx-R9M7lpV_DYdF5s_/view?usp=sharing" target="_blank">
      Google Drive Download
    </a>
  </li>
  <li>
    <strong>UIDAI Hackathon Data Portal:</strong>
    <a href="https://event.data.gov.in/challenge/uidai-data-hackathon-2026/" target="_blank">
      event.data.gov.in
    </a>
  </li>
  <li>
    <strong>Secondary Data Catalog:</strong>
    <a href="https://www.data.gov.in/" target="_blank">
      data.gov.in
    </a>
  </li>
</ul>

<hr>

<p><em>Prepared as part of the UIDAI Data-Driven Innovation Hackathon 2026.</em></p>

</body>
</html>
