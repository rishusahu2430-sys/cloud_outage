import pandas as pd
import numpy as np

df = pd.read_csv("data/cloud_outages_dataset.csv")

# Select numeric columns
numeric_data = df.select_dtypes(include=np.number)

print("Mean using NumPy:")
print(np.mean(numeric_data))

print("\nMedian using NumPy:")
print(np.median(numeric_data))

print("\nStandard Deviation:")
print(np.std(numeric_data))