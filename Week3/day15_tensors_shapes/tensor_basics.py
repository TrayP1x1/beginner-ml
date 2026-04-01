from pathlib import Path

import pandas as pd
import torch


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


def prepare_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    prepared_df = df.copy()
    for column in FEATURE_COLUMNS:
        prepared_df[column] = prepared_df[column].fillna(prepared_df[column].median())
    return prepared_df


def to_float_tensor(values) -> torch.Tensor:
    tensor = torch.tensor(values, dtype=torch.float32)
    return tensor


def describe_tensor(name: str, tensor: torch.Tensor) -> None:
    print(f"{name}: shape={tuple(tensor.shape)}, dtype={tensor.dtype}, device={tensor.device}")


def main() -> None:
    data_path = Path(__file__).resolve().parents[2] / "data" / "student_dev_ai_practice.csv"
    df = prepare_dataframe(load_dataset(data_path))

    X = to_float_tensor(df[FEATURE_COLUMNS].to_numpy())
    y_regression = to_float_tensor(df["test_score"].to_numpy()).reshape(-1, 1)
    y_classification = to_float_tensor(df["passed_test"].to_numpy()).reshape(-1, 1)

    assert X.ndim == 2
    assert y_regression.ndim == 2
    assert y_classification.ndim == 2

    describe_tensor("X", X)
    describe_tensor("y_regression", y_regression)
    describe_tensor("y_classification", y_classification)


if __name__ == "__main__":
    main()
