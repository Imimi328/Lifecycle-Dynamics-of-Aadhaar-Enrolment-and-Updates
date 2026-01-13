import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv(
    "outputs/MasterDataset/master_state_dataset_normalized.csv"
)

# ==============================
# SELECT VARIABLES FOR ANALYSIS
# ==============================
corr_vars = [
    "demo_updates_per_million",
    "biometric_updates_per_million",
    "literacy_rate_2011",
    "migration_persons_2011",
    "population_18_plus_share",
    "per_capita_gsdp"
]

corr_df = df[corr_vars].dropna()

# ==============================
# COMPUTE CORRELATION
# ==============================
correlation_matrix = corr_df.corr(method="pearson")

print("\nCorrelation Matrix:\n")
print(correlation_matrix.round(3))

# ==============================
# OPTIONAL: HEATMAP (VISUAL)
# ==============================
plt.figure(figsize=(10, 8))
plt.imshow(correlation_matrix, cmap="coolwarm", interpolation="nearest")
plt.colorbar()

plt.xticks(range(len(corr_vars)), corr_vars, rotation=45, ha="right")
plt.yticks(range(len(corr_vars)), corr_vars)

plt.title("Correlation Matrix of Aadhaar Update Intensity and State Indicators")
plt.tight_layout()
plt.show()
