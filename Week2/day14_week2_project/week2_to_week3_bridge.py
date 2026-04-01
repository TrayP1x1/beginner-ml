from pathlib import Path

import pandas as pd
import torch
from sklearn.model_selection import train_test_split


FEATURE_COLUMNS = [
    "hours_python",
    "hours_numpy",
    "projects_completed",
    "attendance_rate",
    "practice_tests",
    "sleep_hours",
]


def load_dataset(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path)


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    for column in FEATURE_COLUMNS:
        cleaned[column] = cleaned[column].fillna(cleaned[column].median())
    return cleaned


def split_features_and_target(
    df: pd.DataFrame, target_column: str
) -> tuple[pd.DataFrame, pd.Series]:
    return df[FEATURE_COLUMNS], df[target_column]


def normalize_train_valid(
    X_train: pd.DataFrame, X_valid: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:
    means = X_train.mean()
    stds = X_train.std().replace(0, 1)
    return (X_train - means) / stds, (X_valid - means) / stds


def to_tensor_pair(X: pd.DataFrame, y: pd.Series) -> tuple[torch.Tensor, torch.Tensor]:
    X_tensor = torch.tensor(X.to_numpy(), dtype=torch.float32)
    y_tensor = torch.tensor(y.to_numpy(), dtype=torch.float32).reshape(-1, 1)
    assert X_tensor.ndim == 2
    assert y_tensor.ndim == 2
    return X_tensor, y_tensor


def main() -> None:
    data_path = Path(__file__).resolve().parents[2] / "data" / "student_dev_ai_practice.csv"
    df = clean_dataframe(load_dataset(data_path))
    X, y = split_features_and_target(df, "test_score")

    print("DataFrame shapes:", X.shape, y.shape)

    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    X_train_norm, X_valid_norm = normalize_train_valid(X_train, X_valid)

    print("NumPy shapes:", X_train_norm.to_numpy().shape, y_train.to_numpy().reshape(-1, 1).shape)

    X_train_tensor, y_train_tensor = to_tensor_pair(X_train_norm, y_train)
    X_valid_tensor, y_valid_tensor = to_tensor_pair(X_valid_norm, y_valid)

    print("Tensor train shapes:", tuple(X_train_tensor.shape), tuple(y_train_tensor.shape))
    print("Tensor valid shapes:", tuple(X_valid_tensor.shape), tuple(y_valid_tensor.shape))


if __name__ == "__main__":
    main()
