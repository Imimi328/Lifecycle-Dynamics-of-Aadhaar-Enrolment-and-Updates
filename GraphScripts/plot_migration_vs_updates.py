import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# LOAD NORMALIZED DATASET
# ==============================
df = pd.read_csv(
    "outputs/MasterDataset/master_state_dataset_normalized.csv"
)

# Keep only rows with required data
plot_df = df.dropna(
    subset=["migration_persons_2011", "demo_updates_per_million"]
)

# ==============================
# CREATE SCATTER PLOT
# ==============================
plt.figure(figsize=(12, 8))

plt.scatter(
    plot_df["migration_persons_2011"],
    plot_df["demo_updates_per_million"],
    alpha=0.75
)

# ==============================
# LABEL EACH STATE
# ==============================
for _, row in plot_df.iterrows():
    plt.annotate(
        row["state"],
        (row["migration_persons_2011"], row["demo_updates_per_million"]),
        fontsize=8,
        alpha=0.7,
        xytext=(5, 5),
        textcoords="offset points"
    )

# ==============================
# AXES & TITLE
# ==============================
plt.xlabel("Migration Intensity (Census 2011 Indicator)")
plt.ylabel("Demographic Updates per Million Population")
plt.title(
    "Migration Intensity vs Aadhaar Demographic Update Intensity (State-wise)"
)

plt.grid(True)
plt.tight_layout()

# ==============================
# SHOW PLOT
# ==============================
plt.show()
