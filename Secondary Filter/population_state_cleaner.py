import pandas as pd
from pathlib import Path

# =============================
# PATHS
# =============================
INPUT_FILE = Path("data/secondary/population.csv")
OUTPUT_FILE = Path("outputs/population_state_clean.csv")

# =============================
# STATE NAME MAP (reuse same logic)
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
# FILTER ONLY STATES
# =============================
df = df[df["Category"].str.lower() == "state"]

# =============================
# RENAME & CLEAN
# =============================
df["state"] = df["India/State/Union Territory"].astype(str).str.strip()
df["state"] = df["state"].replace(STATE_MAP)

# Remove India row if present
df = df[df["state"].str.lower() != "india"]

# =============================
# SELECT REQUIRED COLUMNS
# =============================
df_clean = df[[
    "state",
    "Population 2011",
    "Population Density (per sq.km) - 2011"
]].copy()

df_clean.columns = [
    "state",
    "population_2011",
    "population_density_2011"
]

# =============================
# FINAL AGGREGATION (safety)
# =============================
df_clean = (
    df_clean
    .groupby("state", as_index=False)
    .sum()
)

# =============================
# SAVE
# =============================
df_clean.to_csv(OUTPUT_FILE, index=False)
print("Population state-level dataset cleaned successfully.")
