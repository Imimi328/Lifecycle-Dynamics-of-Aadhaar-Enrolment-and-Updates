import pandas as pd
from pathlib import Path

# =============================
# PATHS
# =============================
INPUT_FILE = Path("data/secondary/migration.xlsx")
OUTPUT_FILE = Path("outputs/migration_state_clean.csv")

# =============================
# STATE NAME MAP
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
    "Pondicherry": "Puducherry",
}

# =============================
# LOAD EXCEL
# =============================
df = pd.read_excel(INPUT_FILE)

# =============================
# CLEAN STATE COLUMN
# =============================
df["state"] = df["All India/State/Union Territory"].astype(str).str.strip()
df["state"] = df["state"].replace(STATE_MAP)

# Remove All India row
df = df[df["state"].str.lower() != "all india"]

# =============================
# SELECT 2011 PERSONS DATA
# =============================
df_clean = df[[
    "state",
    "2011 - Rural - Person",
    "2011 - Urban - Persons"
]].copy()

# Convert to numeric
df_clean["2011 - Rural - Person"] = pd.to_numeric(
    df_clean["2011 - Rural - Person"], errors="coerce"
)
df_clean["2011 - Urban - Persons"] = pd.to_numeric(
    df_clean["2011 - Urban - Persons"], errors="coerce"
)

# =============================
# TOTAL MIGRATION PERSONS
# =============================
df_clean["migration_persons_2011"] = (
    df_clean["2011 - Rural - Person"] +
    df_clean["2011 - Urban - Persons"]
)

df_clean = df_clean[["state", "migration_persons_2011"]]

# Drop missing
df_clean = df_clean.dropna(subset=["migration_persons_2011"])

# =============================
# FINAL SAFETY AGGREGATION
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
print("Migration state-level dataset cleaned successfully.")
