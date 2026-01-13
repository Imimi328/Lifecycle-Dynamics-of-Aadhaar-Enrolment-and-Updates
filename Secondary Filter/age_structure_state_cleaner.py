import pandas as pd
from pathlib import Path

# =============================
# PATHS
# =============================
INPUT_FILE = Path("data/secondary/age_structure.xlsx")
OUTPUT_FILE = Path("outputs/age_structure_state_clean.csv")

# =============================
# LOAD DATA
# =============================
df = pd.read_excel(INPUT_FILE)

# =============================
# FILTER STATE-LEVEL ROWS
# =============================
df = df[df["Area Name"].str.startswith("State", na=False)]

# Extract clean state name
df["state"] = (
    df["Area Name"]
    .str.replace(r"State\s*-\s*", "", regex=True)
    .str.replace(r"\s*\(\d+\)", "", regex=True)
    .str.strip()
)

# =============================
# CLEAN AGE COLUMN
# =============================
df = df[~df["Age"].isin(["All ages", "Age not stated"])]

# Convert age to numeric where possible
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# =============================
# TOTAL POPULATION PER STATE
# =============================
total_pop = (
    df.groupby("state", as_index=False)["Total Persons"]
    .sum()
    .rename(columns={"Total Persons": "total_population"})
)

# =============================
# 18+ POPULATION
# =============================
pop_18_plus = (
    df[df["Age"] >= 18]
    .groupby("state", as_index=False)["Total Persons"]
    .sum()
    .rename(columns={"Total Persons": "population_18_plus"})
)

# =============================
# MERGE & COMPUTE SHARE
# =============================
age_struct = pd.merge(total_pop, pop_18_plus, on="state", how="inner")

age_struct["population_18_plus_share"] = (
    age_struct["population_18_plus"] /
    age_struct["total_population"]
)

age_struct = age_struct[["state", "population_18_plus_share"]]

# =============================
# SAVE
# =============================
age_struct.to_csv(OUTPUT_FILE, index=False)
print("Age-structure state-level dataset cleaned successfully.")
