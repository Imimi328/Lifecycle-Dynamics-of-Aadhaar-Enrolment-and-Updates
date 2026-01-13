import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv(
    "outputs/MasterDataset/master_state_dataset_normalized.csv"
)

plot_df = df.dropna(
    subset=[
        "biometric_updates_per_million",
        "demo_updates_per_million"
    ]
)

# ==============================
# SCATTER PLOT
# ==============================
plt.figure(figsize=(12, 8))

plt.scatter(
    plot_df["biometric_updates_per_million"],
    plot_df["demo_updates_per_million"],
    alpha=0.75
)

# ==============================
# LABEL STATES
# ==============================
for _, row in plot_df.iterrows():
    plt.annotate(
        row["state"],
        (
            row["biometric_updates_per_million"],
            row["demo_updates_per_million"]
        ),
        fontsize=8,
        alpha=0.7,
        xytext=(5, 5),
        textcoords="offset points"
    )

# ==============================
# AXES & TITLE
# ==============================
plt.xlabel("Biometric Updates per Million Population")
plt.ylabel("Demographic Updates per Million Population")
plt.title(
    "Biometric vs Demographic Aadhaar Update Intensity (State-wise)"
)

plt.grid(True)
plt.tight_layout()
plt.show()
