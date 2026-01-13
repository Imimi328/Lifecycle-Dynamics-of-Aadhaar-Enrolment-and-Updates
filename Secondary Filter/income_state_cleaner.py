import pandas as pd
from pathlib import Path

# =============================
# CONFIG
# =============================
INPUT_FILE = Path("data/secondary/income.csv")
OUTPUT_FILE = Path("outputs/income_state_clean.csv")

# CHANGE THIS if income file is state-specific
DEFAULT_STATE = "Karnataka"

# =============================
# LOAD DATA
# =============================
df = pd.read_csv(INPUT_FILE)

# =============================
# CLEAN COLUMN NAMES
# =============================
df.columns = df.columns.str.strip()

# =============================
# SELECT PER CAPITA INCOME (2018-19)
# =============================
income_col = "Per capita income in Rs_2018_19_At Current Prices"

df = df[["taluk_name", income_col]].copy()

# Convert to numeric
df[income_col] = pd.to_numeric(df[income_col], errors="coerce")

# Drop zero / missing income rows
df = df[df[income_col] > 0]

# =============================
# ADD STATE COLUMN
# =============================
# If your file already has a state column, comment this line
df["state"] = DEFAULT_STATE

# =============================
# AGGREGATE TO STATE LEVEL
# =============================
state_income = (
    df.groupby("state", as_index=False)[income_col]
    .mean()
)

state_income.rename(
    columns={income_col: "per_capita_income_2018_19"},
    inplace=True
)

# =============================
# SAVE
# =============================
state_income.to_csv(OUTPUT_FILE, index=False)
print("Income state-level dataset cleaned successfully.")
