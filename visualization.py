# src/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns


def plot_correlation(df):
    """Correlation heatmap"""
    numeric_df = df.select_dtypes(include='number')

    plt.figure(figsize=(12, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()


def plot_region_count(df):
    """Region countplot"""
    if 'Region' in df.columns:
        plt.figure(figsize=(8, 5))
        sns.countplot(data=df, x='Region')
        plt.xticks(rotation=45)
        plt.title("Outages by Region")
        plt.show()


def plot_distribution(df, column):
    """Histogram for numeric column"""
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribution of {column}")
    plt.show()

