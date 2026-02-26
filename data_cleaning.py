# src/data_cleaning.py

import pandas as pd
import numpy as np


def load_data(path):
    """Load dataset"""
    df = pd.read_csv(path)
    return df


def clean_data(df):
    """Perform data cleaning"""

    # Remove extra spaces in column names
    df.columns = df.columns.str.strip()

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    num_cols = df.select_dtypes(include=np.number).columns
    cat_cols = df.select_dtypes(include='object').columns

    for col in num_cols:
        df[col].fillna(df[col].median(), inplace=True)

    for col in cat_cols:
        df[col].fillna(df[col].mode()[0], inplace=True)

    # Remove outliers using IQR
    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        df = df[(df[col] >= lower) & (df[col] <= upper)]

    df.reset_index(drop=True, inplace=True)

    return df
