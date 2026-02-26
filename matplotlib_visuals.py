import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cloud_outages_dataset.csv")

# Histogram
df.hist(figsize=(10,8))
plt.suptitle("Histogram of Numeric Features")
plt.show()

# Line Plot Example (if dataset has date column)
# df.plot(x='Date', y='Downtime_Minutes')
# plt.show()