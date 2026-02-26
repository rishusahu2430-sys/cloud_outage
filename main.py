# main.py

from src.data_cleaning import load_data, clean_data
from src.data_transformation import feature_engineering, encode_data
from src.visualization import plot_correlation, plot_region_count

# Load data
df = load_data("data/cloud_outages_dataset.csv")

# Clean data
df = clean_data(df)

# Transform data
df = feature_engineering(df)
df = encode_data(df)

# Save cleaned data
df.to_csv("cleaned_cloud_outages.csv", index=False)

# Visualizations
plot_correlation(df)
plot_region_count(df)

print("Project executed successfully!")

