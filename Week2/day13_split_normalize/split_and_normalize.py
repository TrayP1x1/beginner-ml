from dataclasses import dataclass
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

FEATURE_COLUMNS = [
    "hours_python",
    "hours_numpy",
    "projects_completed",
    "attendance_rate",
    "practice_tests",
    "sleep_hours",
]


@dataclass(frozen=True)
class NormalizationStats:
    means: dict[str, float]
    stds: dict[str, float]


def load_dataset(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path)


def clean_numeric_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = df.copy()
    for column in FEATURE_COLUMNS:
        cleaned_df[column] = cleaned_df[column].fillna(cleaned_df[column].median())
    return cleaned_df


def split_dataset(
    df: pd.DataFrame, target_column: str
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.Series, pd.Series, pd.Series]:
    X = df[FEATURE_COLUMNS]
    y = df[target_column]

    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.4, random_state=42
    )
    X_valid, X_test, y_valid, y_test = train_test_split(
        X_temp, y_temp, test_size=0.5, random_state=42
    )
    return X_train, X_valid, X_test, y_train, y_valid, y_test


def fit_normalization_stats(X_train: pd.DataFrame) -> NormalizationStats:
    means = {column: float(X_train[column].mean()) for column in X_train.columns}
    stds = {
        column: (
            float(X_train[column].std()) if float(X_train[column].std()) != 0.0 else 1.0
        )
        for column in X_train.columns
    }
    return NormalizationStats(means=means, stds=stds)


def apply_normalization(X: pd.DataFrame, stats: NormalizationStats) -> pd.DataFrame:
    normalized = X.copy()
    for column in normalized.columns:
        normalized[column] = (normalized[column] - stats.means[column]) / stats.stds[
            column
        ]
    return normalized


def main() -> None:
    data_path = (
        Path(__file__).resolve().parents[2] / "data" / "student_dev_ai_practice.csv"
    )
    df = clean_numeric_missing_values(load_dataset(data_path))
    X_train, X_valid, X_test, y_train, y_valid, y_test = split_dataset(df, "test_score")

    stats = fit_normalization_stats(X_train)
    X_train_norm = apply_normalization(X_train, stats)
    X_valid_norm = apply_normalization(X_valid, stats)
    X_test_norm = apply_normalization(X_test, stats)

    print("train shape:", X_train_norm.shape, y_train.shape)
    print("valid shape:", X_valid_norm.shape, y_valid.shape)
    print("test shape:", X_test_norm.shape, y_test.shape)
    print("normalization means:", stats.means)


if __name__ == "__main__":
    main()
