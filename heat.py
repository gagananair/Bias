import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================
# LOAD CSV
# ==========================

df = pd.read_csv("Heatplotown.csv")

# ==========================
# CATEGORY -> SCORE
# ==========================

score_map = {
    "High": 1,
    "high":1,
    "Other": 0,
    "other":0,
    "Low": -1,
    "low":-1,
    "CasteIdentity": -1
}

df["Score"] = df["category"].map(score_map)

# Remove rows with unknown categories
df = df.dropna(subset=["Score"])

# ==========================
# ORDER OF NAMES
# ==========================

firstname_order = ["Ramu", "Raju", "Ramesh", "Suresh"]
surname_order = ["Sharma", "Iyer", "Mukherjee",
                 "Valmiki", "Paswan", "Chamar"]

models = df["Model"].unique()

# ==========================
# CREATE SUBPLOTS
# ==========================

fig, axes = plt.subplots(
    1,
    len(models),
    figsize=(7 * len(models), 6),
    constrained_layout=True
)

if len(models) == 1:
    axes = [axes]

# ==========================
# HEATMAP FOR EACH MODEL
# ==========================

for ax, model in zip(axes, models):

    temp = df[df["Model"] == model]

    heat = temp.pivot_table(
        index="Firstname",
        columns="surname",
        values="Score",
        aggfunc="mean"
    )

    heat = heat.reindex(index=firstname_order,
                        columns=surname_order)

    sns.heatmap(
        heat,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        linewidths=0.5,
        linecolor="white",
        cbar=(ax == axes[-1]),
        ax=ax
    )

    ax.set_title(model, fontsize=15)
    ax.set_xlabel("Surname")
    ax.set_ylabel("FirstName")

    # Vertical separator between caste groups
    ax.axvline(3, color="black", linewidth=2)

plt.suptitle(
    "First Name × Surname, per Model",
    fontsize=18
)

# Save as PNG
plt.savefig(
    "Occupation_PrestigeHeatmap.png",
    dpi=300,
    bbox_inches="tight"
)

# Display the figure
plt.show()

# Optional: free memory
plt.close()