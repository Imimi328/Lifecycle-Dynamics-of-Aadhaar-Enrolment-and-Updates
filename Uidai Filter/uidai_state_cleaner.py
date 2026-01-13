import pandas as pd
from pathlib import Path

# =============================
# CONFIG
# =============================
INPUT_DIR = Path("outputs")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

# =============================
# STATE NAME CORRECTION MAP
# =============================
STATE_MAP = {
    # Andaman
    "Andaman & Nicobar Islands": "Andaman and Nicobar Islands",
    "Andaman and Nicobar Islands": "Andaman and Nicobar Islands",

    # Andhra
    "Andhra Pradesh": "Andhra Pradesh",
    "andhra pradesh": "Andhra Pradesh",

    # Odisha
    "ODISHA": "Odisha",
    "Odisha": "Odisha",
    "Orissa": "Odisha",
    "odisha": "Odisha",

    # West Bengal
    "WEST BENGAL": "West Bengal",
    "West Bengal": "West Bengal",
    "West  Bengal": "West Bengal",
    "West Bangal": "West Bengal",
    "West bengal": "West Bengal",
    "Westbengal": "West Bengal",
    "WESTBENGAL": "West Bengal",
    "West Bengli": "West Bengal",

    # Jammu & Kashmir
    "Jammu & Kashmir": "Jammu and Kashmir",
    "Jammu and Kashmir": "Jammu and Kashmir",
    "Jammu And Kashmir": "Jammu and Kashmir",

    # Chhattisgarh
    "Chhatisgarh": "Chhattisgarh",
    "Chhattisgarh": "Chhattisgarh",

    # Dadra & Daman
    "Dadra & Nagar Haveli": "Dadra and Nagar Haveli and Daman and Diu",
    "Dadra and Nagar Haveli": "Dadra and Nagar Haveli and Daman and Diu",
    "Daman & Diu": "Dadra and Nagar Haveli and Daman and Diu",
    "Daman and Diu": "Dadra and Nagar Haveli and Daman and Diu",
    "The Dadra And Nagar Haveli And Daman And Diu": "Dadra and Nagar Haveli and Daman and Diu",
    "Dadra and Nagar Haveli and Daman and Diu": "Dadra and Nagar Haveli and Daman and Diu",

    # Puducherry
    "Pondicherry": "Puducherry",
    "Puducherry": "Puducherry",

    # Uttarakhand
    "Uttaranchal": "Uttarakhand",
    "Uttarakhand": "Uttarakhand",
}

# =============================
# CLEAN & AGGREGATE FUNCTION
# =============================
def clean_and_aggregate(input_file, value_cols, output_file):
    df = pd.read_csv(input_file)

    # Normalize state column
    df["state"] = df["state"].astype(str).str.strip()

    # Apply correction mapping (only where needed)
    df["state"] = df["state"].replace(STATE_MAP)

    # Remove junk rows (numeric-only, empty)
    df = df[~df["state"].str.match(r"^\d+$", na=False)]
    df = df[df["state"].str.len() > 2]

    # Aggregate
    cleaned = (
        df.groupby("state", as_index=False)[value_cols]
        .sum()
    )

    cleaned.to_csv(output_file, index=False)
    print(f"Saved: {output_file}")

# =============================
# RUN FOR ALL UIDAI DATASETS
# =============================

# Enrolment
clean_and_aggregate(
    INPUT_DIR / "uidai_enrolment_state.csv",
    ["age_0_5", "age_5_17", "age_18_greater", "total_enrolments"],
    OUTPUT_DIR / "uidai_enrolment_state_clean.csv"
)

# Demographic updates
clean_and_aggregate(
    INPUT_DIR / "uidai_demographic_state.csv",
    ["demo_age_5_17", "demo_age_17_", "total_demographic_updates"],
    OUTPUT_DIR / "uidai_demographic_state_clean.csv"
)

# Biometric updates
clean_and_aggregate(
    INPUT_DIR / "uidai_biometric_state.csv",
    ["bio_age_5_17", "bio_age_17_", "total_biometric_updates"],
    OUTPUT_DIR / "uidai_biometric_state_clean.csv"
)

print("\nUIDAI STATE CLEANING COMPLETED SUCCESSFULLY.")
