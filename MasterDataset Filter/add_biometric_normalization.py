import pandas as pd

df = pd.read_csv(
    "outputs/MasterDataset/master_state_dataset_normalized.csv"
)

df["biometric_updates_per_million"] = (
    df["total_biometric_updates"] / df["population_2011"]
) * 1_000_000

df.to_csv(
    "outputs/MasterDataset/master_state_dataset_normalized.csv",
    index=False
)

print("Biometric normalization added.")
