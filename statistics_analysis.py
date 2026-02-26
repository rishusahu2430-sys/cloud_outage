import pandas as pd
import statistics

df = pd.read_csv("data/cloud_outages_dataset.csv")

# Example column (change according to dataset)
col = df.select_dtypes(include='number').columns[0]

data = df[col].dropna()

print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))
print("Standard Deviation:", statistics.stdev(data))