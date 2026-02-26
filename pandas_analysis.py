import pandas as pd

# Load dataset
df = pd.read_csv("data/cloud_outages_dataset.csv")

# Show first rows
print("First 5 Rows:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())s