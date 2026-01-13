import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "outputs/MasterDataset/master_state_dataset_normalized.csv"
)

plot_df = df.dropna(
    subset=["population_18_plus_share", "demo_updates_per_million"]
)

plt.figure(figsize=(11, 7))
plt.scatter(
    plot_df["population_18_plus_share"],
    plot_df["demo_updates_per_million"],
    alpha=0.75
)

for _, row in plot_df.iterrows():
    plt.annotate(
        row["state"],
        (row["population_18_plus_share"], row["demo_updates_per_million"]),
        fontsize=8,
        alpha=0.7
    )

plt.xlabel("Share of Population Aged 18 and Above")
plt.ylabel("Demographic Updates per Million Population")
plt.title("Adult Population Share vs Aadhaar Demographic Update Intensity")

plt.grid(True)
plt.tight_layout()
plt.show()
