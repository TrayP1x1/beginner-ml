from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass(frozen=True)
class DatasetSummary:
    row_count: int
    column_count: int
    column_names: list[str]
    numeric_columns: list[str]
    missing_counts: dict[str, int]
    target_column: str


def load_dataset(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file does not exist: {csv_path}")

    dataframe = pd.read_csv(csv_path)
    if dataframe.empty:
        raise ValueError(f"Dataset is empty: {csv_path}")

    return dataframe


def validate_target_column(df: pd.DataFrame, target_column: str) -> None:
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in dataset.")


def build_dataset_summary(df: pd.DataFrame, target_column: str) -> DatasetSummary:
    validate_target_column(df, target_column)

    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    missing_counts = {column: int(count) for column, count in df.isna().sum().items()}

    return DatasetSummary(
        row_count=len(df),
        column_count=len(df.columns),
        column_names=df.columns.tolist(),
        numeric_columns=numeric_columns,
        missing_counts=missing_counts,
        target_column=target_column,
    )


def print_dataset_summary(summary: DatasetSummary, preview_df: pd.DataFrame) -> None:
    print("shape:", (summary.row_count, summary.column_count))
    print("columns:", summary.column_names)
    print("numeric columns:", summary.numeric_columns)
    print("missing values:", summary.missing_counts)
    print("target column:", summary.target_column)
    print()
    print("head:")
    print(preview_df.head())


def fill_numeric_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = df.copy()
    numeric_columns = cleaned_df.select_dtypes(include="number").columns

    for column in numeric_columns:
        cleaned_df[column] = cleaned_df[column].fillna(cleaned_df[column].median())

    return cleaned_df


def prepare_features_and_target(
    df: pd.DataFrame, target_column: str
) -> tuple[pd.DataFrame, pd.Series]:
    validate_target_column(df, target_column)

    cleaned_df = fill_numeric_missing_values(df)
    feature_df = cleaned_df.drop(columns=[target_column])
    if feature_df.empty:
        raise ValueError("Feature set is empty after removing the target column.")

    feature_df = pd.get_dummies(feature_df, drop_first=True)
    target_series = cleaned_df[target_column]

    return feature_df, target_series
