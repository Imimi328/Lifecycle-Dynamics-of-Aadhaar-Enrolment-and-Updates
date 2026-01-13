import pandas as pd
import glob
from pathlib import Path

# =============================
# PATHS
# =============================
BASE_DIR = Path("data/uidai")
OUT_DIR = Path("outputs")
OUT_DIR.mkdir(exist_ok=True)

# =============================
# HELPER FUNCTION
# =============================
def load_and_combine(folder):
    files = glob.glob(str(folder / "*.csv"))
    if not files:
        raise FileNotFoundError(f"No CSV files found in {folder}")
    return pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# =============================
# ENROLMENT DATA
# =============================
enrol = load_and_combine(BASE_DIR / "enrolment")

enrol_state = (
    enrol.groupby("state", as_index=False)
    .agg({
        "age_0_5": "sum",
        "age_5_17": "sum",
        "age_18_greater": "sum"
    })
)

enrol_state["total_enrolments"] = (
    enrol_state["age_0_5"] +
    enrol_state["age_5_17"] +
    enrol_state["age_18_greater"]
)

enrol_state.to_csv(OUT_DIR / "uidai_enrolment_state.csv", index=False)

# =============================
# DEMOGRAPHIC UPDATES
# =============================
demo = load_and_combine(BASE_DIR / "demographic")

demo_state = (
    demo.groupby("state", as_index=False)
    .agg({
        "demo_age_5_17": "sum",
        "demo_age_17_": "sum"
    })
)

demo_state["total_demographic_updates"] = (
    demo_state["demo_age_5_17"] +
    demo_state["demo_age_17_"]
)

demo_state.to_csv(OUT_DIR / "uidai_demographic_state.csv", index=False)

# =============================
# BIOMETRIC UPDATES
# =============================
bio = load_and_combine(BASE_DIR / "biometric")

bio_state = (
    bio.groupby("state", as_index=False)
    .agg({
        "bio_age_5_17": "sum",
        "bio_age_17_": "sum"
    })
)

bio_state["total_biometric_updates"] = (
    bio_state["bio_age_5_17"] +
    bio_state["bio_age_17_"]
)

bio_state.to_csv(OUT_DIR / "uidai_biometric_state.csv", index=False)

print("UIDAI STATE-LEVEL FILES CREATED SUCCESSFULLY.")
