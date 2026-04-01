from pathlib import Path

import pandas as pd


def load_dataset(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path)


def print_dataset_summary(df: pd.DataFrame, target_column: str) -> None:
    print("shape:", df.shape)
    print("columns:", list(df.columns))
    print("missing values:")
    print(df.isna().sum())
    print("target column:", target_column)
    print()
    print("head:")
    print(df.head())


def prepare_features_and_target(
    df: pd.DataFrame, target_column: str
) -> tuple[pd.DataFrame, pd.Series]:
    cleaned_df = df.copy()

    numeric_columns = cleaned_df.select_dtypes(include="number").columns
    for column in numeric_columns:
        cleaned_df[column] = cleaned_df[column].fillna(cleaned_df[column].median())

    if target_column not in cleaned_df.columns:
        raise ValueError(f"Target column '{target_column}' not found in dataset.")

    feature_df = cleaned_df.drop(columns=[target_column])
    feature_df = pd.get_dummies(feature_df, drop_first=True)
    target_series = cleaned_df[target_column]

    return feature_df, target_series
