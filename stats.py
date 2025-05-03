from collections import Counter
import math

def compute_statistics(all_colors):
    color_counts = Counter(all_colors)
    unique_colors = sorted(color_counts.keys())

    color_to_num = {color: i for i, color in enumerate(unique_colors, start=1)}
    num_to_color = {v: k for k, v in color_to_num.items()}

    numeric_values = [color_to_num[color] for color in all_colors]

    mean_value = sum(numeric_values) / len(numeric_values)
    mean_color_index = round(mean_value)
    mean_color = num_to_color[mean_color_index]

    variance = sum((x - mean_value) ** 2 for x in numeric_values) / len(numeric_values)
    std_dev = math.sqrt(variance)

    red_count = color_counts.get("RED", 0)
    prob_red = red_count / len(numeric_values)

    return {
        "color_counts": color_counts,
        "mean_color": mean_color,
        "variance": variance,
        "std_dev": std_dev,
        "prob_red": prob_red
    }
