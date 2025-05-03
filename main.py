from parser import extract_colors_from_html
from stats import compute_statistics
from db import save_to_database

# Step 1: Parse HTML
colors = extract_colors_from_html("index.html")

# Step 2: Compute stats
stats = compute_statistics(colors)

# Step 3: Print summary
print("Color Frequencies:")
for color, count in stats["color_counts"].items():
    print(f"{color}: {count}")

print(f"\nMean Color (by index): {stats['mean_color']}")
print(f"Variance: {stats['variance']:.2f}")
print(f"Standard Deviation: {stats['std_dev']:.2f}")
print(f"Probability of RED: {stats['prob_red']:.4f}")

# Step 4: Save to MySQL
save_to_database(stats["color_counts"])
