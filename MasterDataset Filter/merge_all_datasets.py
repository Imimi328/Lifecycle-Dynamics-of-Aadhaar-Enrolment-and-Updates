import pandas as pd
from pathlib import Path
from functools import reduce

# =============================
# PATHS
# =============================
DATA_DIR = Path("outputs")
OUTPUT_FILE = DATA_DIR / "master_state_dataset.csv"

# =============================
# FILES TO MERGE
# =============================
files = [
    "uidai_enrolment_state_clean.csv",
    "uidai_demographic_state_clean.csv",
    "uidai_biometric_state_clean.csv",
    "population_state_clean.csv",
    "literacy_state_clean.csv",
    "gsdp_state_clean.csv",
    "migration_state_clean.csv",
    "age_structure_state_clean.csv",
]

# =============================
# LOAD ALL DATAFRAMES
# =============================
dfs = []
for f in files:
    df = pd.read_csv(DATA_DIR / f)
    df["state"] = df["state"].str.strip().str.title()
    dfs.append(df)

# =============================
# MERGE SEQUENTIALLY ON STATE
# =============================
master_df = reduce(
    lambda left, right: pd.merge(left, right, on="state", how="left"),
    dfs
)

# =============================
# SORT FOR READABILITY
# =============================
master_df = master_df.sort_values("state").reset_index(drop=True)

# =============================
# SAVE
# =============================
master_df.to_csv(OUTPUT_FILE, index=False)
print("Master state-level dataset created successfully.")
