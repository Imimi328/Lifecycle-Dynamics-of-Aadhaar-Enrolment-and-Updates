import pandas as pd
from pathlib import Path

# =============================
# PATHS
# =============================
INPUT_FILE = Path("outputs/master_state_dataset.csv")
OUTPUT_FILE = Path("outputs/master_state_dataset_final.csv")

# =============================
# LOAD
# =============================
df = pd.read_csv(INPUT_FILE)

# =============================
# DEFINE COLUMN TYPES
# =============================

UIDAI_SUM_COLS = [
    "age_0_5", "age_5_17", "age_18_greater", "total_enrolments",
    "demo_age_5_17", "demo_age_17_", "total_demographic_updates",
    "bio_age_5_17", "bio_age_17_", "total_biometric_updates"
]

STATIC_MEAN_COLS = [
    "population_2011",
    "population_density_2011",
    "literacy_rate_2011",
    "per_capita_gsdp",
    "migration_persons_2011",
    "population_18_plus_share"
]

# =============================
# AGGREGATE
# =============================
agg_dict = {}

for col in UIDAI_SUM_COLS:
    agg_dict[col] = "sum"

for col in STATIC_MEAN_COLS:
    agg_dict[col] = "mean"

final_df = (
    df
    .groupby("state", as_index=False)
    .agg(agg_dict)
)

# =============================
# SORT
# =============================
final_df = final_df.sort_values("state").reset_index(drop=True)

# =============================
# SAVE
# =============================
final_df.to_csv(OUTPUT_FILE, index=False)
print("Final master dataset cleaned successfully.")
