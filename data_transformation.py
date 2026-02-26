# src/data_transformation.py

import pandas as pd
from sklearn.preprocessing import StandardScaler


def feature_engineering(df):
    """Create new features"""

    if 'system_load_after_outage' in df.columns:
        df['system_load_before_outage'] = (
            df['system_load_after_outage'] / 60
        )

    return df


def encode_data(df):
    """Encode categorical variables"""
    df = pd.get_dummies(df, drop_first=True)
    return df


def scale_data(df):
    """Scale numerical columns"""
    scaler = StandardScaler()

    num_cols = df.select_dtypes(include='number').columns
    df[num_cols] = scaler.fit_transform(df[num_cols])

    return df
