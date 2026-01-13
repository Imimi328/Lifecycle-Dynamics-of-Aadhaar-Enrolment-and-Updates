import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    r"outputs\MasterDataset\master_state_dataset_normalized.csv"
)

# Keep only required columns
df = df[
    ["state", "demo_updates_per_million", "biometric_updates_per_million"]
].dropna()

# Compute medians (same logic as scatter)
x_med = df["demo_updates_per_million"].median()
y_med = df["biometric_updates_per_million"].median()

# Classification function
def classify(row):
    if row["demo_updates_per_million"] < x_med and row["biometric_updates_per_million"] >= y_med:
        return "Type I – Administrative-heavy"
    elif row["demo_updates_per_million"] >= x_med and row["biometric_updates_per_million"] >= y_med:
        return "Type II – Lifecycle-driven"
    elif row["demo_updates_per_million"] >= x_med and row["biometric_updates_per_million"] < y_med:
        return "Type III – High-stress"
    else:
        return "Type IV – Low-interaction"

# Apply classification
df["Aadhaar Interaction Typology"] = df.apply(classify, axis=1)

# Sort for readability
df = df.sort_values(
    by=["Aadhaar Interaction Typology", "state"]
)

# Prepare table data
table_data = df[
    ["state", "Aadhaar Interaction Typology"]
].values.tolist()

column_labels = ["State / UT", "Assigned Typology"]

# ---- Plot table ----
fig, ax = plt.subplots(figsize=(14, len(table_data) * 0.35 + 2))
ax.axis("off")

table = ax.table(
    cellText=table_data,
    colLabels=column_labels,
    loc="center",
    cellLoc="left",
)

# Formatting
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.2)

# Header styling
for (row, col), cell in table.get_celld().items():
    if row == 0:
        cell.set_text_props(weight="bold")
        cell.set_height(0.05)

plt.title(
    "Complete State-Level Typology of Aadhaar Update Behaviour\n"
    "(Derived from Median-Normalized Update Intensities)",
    fontsize=14,
    pad=20
)

plt.tight_layout()

# Save as image for paper / appendix
plt.savefig(
    "outputs/aadhaar_state_typology_table.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
