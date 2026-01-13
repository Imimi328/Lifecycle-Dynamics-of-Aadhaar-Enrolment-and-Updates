import pandas as pd
from pathlib import Path

# =============================
# PATHS
# =============================
INPUT_FILE = Path("data/secondary/gsdp.csv")
OUTPUT_FILE = Path("outputs/gsdp_state_clean.csv")

# =============================
# STATE NAME MAP (reuse logic)
# =============================
STATE_MAP = {
    "Chhatisgarh": "Chhattisgarh",
    "ODISHA": "Odisha",
    "Orissa": "Odisha",
    "WEST BENGAL": "West Bengal",
    "West bengal": "West Bengal",
    "Uttaranchal": "Uttarakhand",
    "Jammu & Kashmir": "Jammu and Kashmir",
    "Jammu And Kashmir": "Jammu and Kashmir",
}

# =============================
# LOAD DATA
# =============================
df = pd.read_csv(INPUT_FILE)

# =============================
# CLEAN STATE COLUMN
# =============================
df["state"] = df["State"].astype(str).str.strip()
df["state"] = df["state"].replace(STATE_MAP)

# =============================
# SELECT GSDP COLUMNS (LATEST FIRST)
# =============================
gsdp_cols = [
    "Per Capita GSDP - 2023-24",
    "Per Capita GSDP - 2022-23",
    "Per Capita GSDP - 2021-22"
]

df_gsdp = df[["state"] + gsdp_cols].copy()

# Convert to numeric
for col in gsdp_cols:
    df_gsdp[col] = pd.to_numeric(df_gsdp[col], errors="coerce")

# =============================
# PICK LATEST AVAILABLE VALUE
# =============================
df_gsdp["per_capita_gsdp"] = (
    df_gsdp[gsdp_cols]
    .bfill(axis=1)
    .iloc[:, 0]
)

df_gsdp = df_gsdp[["state", "per_capita_gsdp"]]

# Drop rows where still missing
df_gsdp = df_gsdp.dropna(subset=["per_capita_gsdp"])

# =============================
# FINAL SAFETY AGGREGATION
# =============================
df_gsdp = (
    df_gsdp
    .groupby("state", as_index=False)
    .mean()
)

# =============================
# SAVE
# =============================
df_gsdp.to_csv(OUTPUT_FILE, index=False)
print("GSDP state-level dataset cleaned successfully.")
