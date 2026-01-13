import pandas as pd

# Load dataset
df = pd.read_csv(
    "outputs/MasterDataset/master_state_dataset_final.csv"
)

# Normalize demographic updates per million population
df["demo_updates_per_million"] = (
    df["total_demographic_updates"] / df["population_2011"]
) * 1_000_000

# Save updated dataset
df.to_csv(
    "outputs/MasterDataset/master_state_dataset_normalized.csv",
    index=False
)

print("Normalized dataset saved successfully.")
