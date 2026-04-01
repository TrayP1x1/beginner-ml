from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass(frozen=True)
class PreparedData:
    features: pd.DataFrame
    target: pd.Series


def load_dataset(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    dataframe = pd.read_csv(csv_path)
    if dataframe.empty:
        raise ValueError("Dataset is empty.")
    return dataframe


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = df.copy()
    numeric_columns = cleaned_df.select_dtypes(include="number").columns
    for column in numeric_columns:
        cleaned_df[column] = cleaned_df[column].fillna(cleaned_df[column].median())
    return cleaned_df


def prepare_features(df: pd.DataFrame, target_column: str) -> PreparedData:
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found.")

    cleaned_df = clean_dataframe(df)
    feature_frame = cleaned_df.drop(columns=[target_column])
    feature_frame = pd.get_dummies(feature_frame, drop_first=True)
    target_series = cleaned_df[target_column]
    return PreparedData(features=feature_frame, target=target_series)
