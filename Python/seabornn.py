import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
# print(sns.get_dataset_names())
# tips = sns.load_dataset("tips")
# iris = sns.load_dataset("iris")
# titanic = sns.load_dataset("titanic")
# planets = sns.load_dataset("planets")
# print(tips)
# # Create the scatterplot
# plt.figure(figsize=(10, 6))
# scatter = sns.scatterplot(x="tip", y="total_bill", data=tips, hue='day')
# # Format the y-axis to display dollar signs
# def format_dollars(x, pos):
#     return f"${x:.2f}"
# # Apply the formatter to the y-axis
# plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(format_dollars))
# plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(format_dollars))
# # Update axis labels
# plt.xlabel('Tip Amount ($)')
# plt.ylabel('Total Bill ($)')
# plt.title('Tips vs Total Bill')
# sns.histplot(tips['tip'], kde=False, bins=30, color='blue', alpha=0.5)
# sns.boxplot(x='sex', y='total_bill', data=tips, hue='day', palette='YlGnBu')
# sns.stripplot(x='sex', y='tip', data=tips, hue='day', palette='YlGnBu', dodge=True)
# sns.jointplot(x="tip", y="total_bill", data=tips, kind='reg', palette='YlGnBu')
# sns.jointplot(x="tip", y="total_bill", data=tips, kind='kde', palette='YlGnBu', shade=True, cmap='YlGnBu')
# sns.jointplot(x="tip", y="total_bill", data=tips, kind='hex', palette='YlGnBu', cmap='YlGnBu')

# sns.pairplot(titanic.select_dtypes(['number']), hue='pclass')
# sns.heatmap(titanic.select_dtypes(include=['number']).corr(), annot=True, cmap='coolwarm', fmt='.2f')
#clustermap
# plt.subplot(3, 3, 1)
# sns.violinplot(data=titanic, x="class", y="age", hue="sex", split=True)
# plt.title("Violin Plot: Age Distribution by Class")
# plt.show()

# Set random seed for reproducibility
np.random.seed(42)

# Generate sample data
df = pd.DataFrame({
    "X": np.arange(1, 21),
    "Y1": np.random.uniform(10, 50, 20),
    "Y2": np.random.uniform(30, 80, 20)
})

# Set Seaborn style and context
sns.set_style("darkgrid")  # Options: white, dark, whitegrid, darkgrid, ticks
sns.set_context("notebook", font_scale=1.3)  # Options: paper, notebook, talk, poster
sns.set_palette("viridis")  # Custom color palette

# Create figure
fig, ax = plt.subplots(figsize=(12, 7), dpi=100)

# Plot with full customization
sns.lineplot(x="X", y="Y1", data=df, marker="o", markersize=10, markeredgewidth=2,
             markeredgecolor="black", markerfacecolor="yellow", linewidth=2.5, alpha=0.8, label="Dataset 1")

sns.lineplot(x="X", y="Y2", data=df, marker="s", markersize=10, markeredgewidth=2,
             markeredgecolor="black", markerfacecolor="red", linewidth=2.5, linestyle="dotted", alpha=0.8, label="Dataset 2")

# Add title and labels with color and font settings
plt.title("Fully Customized Seaborn Line Plot", fontsize=18, fontweight="bold", color="navy", pad=20)
plt.xlabel("X Axis", fontsize=14, fontweight="bold", color="darkred", labelpad=10)
plt.ylabel("Y Axis", fontsize=14, fontweight="bold", color="darkgreen", labelpad=10)

# Customizing the grid
ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.6, color="gray")

# Adjust spines (border lines)
ax.spines["top"].set_visible(False)   # Hide top spine
ax.spines["right"].set_visible(False) # Hide right spine
ax.spines["left"].set_linewidth(1.5)  # Make left spine thicker
ax.spines["bottom"].set_linewidth(1.5) # Make bottom spine thicker

# Customizing ticks
ax.tick_params(axis="x", direction="out", length=6, width=2, colors="darkblue", labelsize=12, rotation=30)
ax.tick_params(axis="y", direction="out", length=6, width=2, colors="darkgreen", labelsize=12)

# Custom Legend with Border and Shadow
legend = plt.legend(title="Legend", title_fontsize=13, fontsize=12, loc="upper left",
                    frameon=True, shadow=True, borderpad=1.2, labelspacing=1.2)
legend.get_frame().set_edgecolor("black")  # Black border for the legend

# Adding annotations (highlighting specific points)
ax.annotate("Highest Point", xy=(df["X"].iloc[df["Y2"].idxmax()], df["Y2"].max()),
            xytext=(15, df["Y2"].max() + 5),
            arrowprops=dict(facecolor="black", shrink=0.05, linewidth=1.5),
            fontsize=12, color="black", fontweight="bold")

# Adjust layout to prevent overlapping
plt.tight_layout()

# # Show the plot
# plt.show()

# # Load dataset
# penguins = sns.load_dataset("penguins")

# # Drop NaN values
# penguins = penguins.dropna()

# # Set figure size
# plt.figure(figsize=(10, 6))

# # Create a scatter plot with KDE overlay
# sns.kdeplot(
#     data=penguins,
#     x="bill_length_mm",
#     y="bill_depth_mm",
#     hue="species",
#     fill=True,
#     alpha=0.4,
# )
# sns.scatterplot(
#     data=penguins,
#     x="bill_length_mm",
#     y="bill_depth_mm",
#     hue="species",
#     edgecolor="black"
# )

# # Titles and labels
# plt.title("Penguin Bill Dimensions: ((Kernel Density Estimation) KDE and Scatter Plot", fontsize=14)
# plt.xlabel("Bill Length (mm)", fontsize=12)
# plt.ylabel("Bill Depth (mm)", fontsize=12)
# plt.legend(title="Species")
# plt.grid(True)

# # Show plot
# plt.show()
