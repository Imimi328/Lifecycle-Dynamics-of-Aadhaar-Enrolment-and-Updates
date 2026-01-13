import pandas as pd
from pathlib import Path

# =============================
# PATHS
# =============================
INPUT_FILE = Path("data/secondary/literacy.csv")
OUTPUT_FILE = Path("outputs/literacy_state_clean.csv")

# =============================
# STATE NAME MAP (same logic as before)
# =============================
STATE_MAP = {
    "Andaman & Nicobar Islands": "Andaman and Nicobar Islands",
    "Andaman and Nicobar Islands": "Andaman and Nicobar Islands",
    "andhra pradesh": "Andhra Pradesh",
    "ODISHA": "Odisha",
    "Orissa": "Odisha",
    "odisha": "Odisha",
    "WEST BENGAL": "West Bengal",
    "West bengal": "West Bengal",
    "West  Bengal": "West Bengal",
    "West Bangal": "West Bengal",
    "Westbengal": "West Bengal",
    "WESTBENGAL": "West Bengal",
    "Jammu & Kashmir": "Jammu and Kashmir",
    "Jammu And Kashmir": "Jammu and Kashmir",
    "Uttaranchal": "Uttarakhand",
    "Chhatisgarh": "Chhattisgarh",
    "Pondicherry": "Puducherry",
}

# =============================
# LOAD DATA
# =============================
df = pd.read_csv(INPUT_FILE)

# =============================
# CLEAN STATE COLUMN
# =============================
df["state"] = df["State/ UTs"].astype(str).str.strip()
df["state"] = df["state"].replace(STATE_MAP)

# Remove India row if present
df = df[df["state"].str.lower() != "india"]

# =============================
# SELECT LATEST YEAR (2011)
# =============================
df_clean = df[["state", "2011"]].copy()
df_clean.rename(columns={"2011": "literacy_rate_2011"}, inplace=True)

# Convert to numeric
df_clean["literacy_rate_2011"] = pd.to_numeric(
    df_clean["literacy_rate_2011"],
    errors="coerce"
)

# Drop rows where literacy is missing
df_clean = df_clean.dropna(subset=["literacy_rate_2011"])

# =============================
# FINAL SAFETY AGGREGATION
# =============================
df_clean = (
    df_clean
    .groupby("state", as_index=False)
    .mean()
)

# =============================
# SAVE
# =============================
df_clean.to_csv(OUTPUT_FILE, index=False)
print("Literacy state-level dataset cleaned successfully.")
