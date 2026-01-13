import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"outputs\MasterDataset\master_state_dataset_normalized.csv")

df = df[
    ["state", "demo_updates_per_million", "biometric_updates_per_million"]
].dropna()

x_med = df["demo_updates_per_million"].median()
y_med = df["biometric_updates_per_million"].median()

plt.figure(figsize=(14, 9))

# Scatter
plt.scatter(
    df["demo_updates_per_million"],
    df["biometric_updates_per_million"],
    s=120,
    alpha=0.7,
    edgecolors="black"
)

# Label only key states (extremes + exemplars)
key_states = [
    "Manipur", "Chhattisgarh", "West Bengal", "Maharashtra",
    "Kerala", "Bihar", "Uttar Pradesh", "Tamil Nadu"
]

for _, r in df[df["state"].isin(key_states)].iterrows():
    plt.text(
        r["demo_updates_per_million"] + 800,
        r["biometric_updates_per_million"] + 800,
        r["state"],
        fontsize=11,
        weight="bold"
    )

# Quadrant lines
plt.axvline(x_med, linestyle="--", linewidth=1.5)
plt.axhline(y_med, linestyle="--", linewidth=1.5)

# Quadrant titles
plt.text(x_med * 1.05, y_med * 1.05, "Type II\nLifecycle-driven", fontsize=12)
plt.text(x_med * 0.55, y_med * 1.05, "Type I\nAdministrative-heavy", fontsize=12)
plt.text(x_med * 0.55, y_med * 0.55, "Type IV\nLow-interaction", fontsize=12)
plt.text(x_med * 1.05, y_med * 0.55, "Type III\nHigh-stress", fontsize=12)

plt.xlabel("Demographic Updates per Million Population", fontsize=12)
plt.ylabel("Biometric Updates per Million Population", fontsize=12)
plt.title("State Typology of Aadhaar Update Behaviour (Normalized)", fontsize=14)

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
