from dataclasses import dataclass
from pathlib import Path

import pandas as pd
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

FEATURE_COLUMNS = [
    "hours_python",
    "hours_numpy",
    "projects_completed",
    "attendance_rate",
    "practice_tests",
    "sleep_hours",
]


@dataclass(frozen=True)
class TrainingConfig:
    data_path: Path
    target_column: str = "test_score"
    learning_rate: float = 0.01
    epochs: int = 50
    batch_size: int = 32


def load_data(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"Missing dataset: {csv_path}")
    df = pd.read_csv(csv_path)
    if df.empty:
        raise ValueError("Dataset is empty.")
    return df


def prepare_features(
    df: pd.DataFrame, target_column: str
) -> tuple[pd.DataFrame, pd.Series]:
    if target_column not in df.columns:
        raise ValueError(f"Missing target column: {target_column}")

    prepared_df = df.copy()
    for column in FEATURE_COLUMNS:
        prepared_df[column] = prepared_df[column].fillna(prepared_df[column].median())
    prepared_df["total_study_hours"] = (
        prepared_df["hours_python"] + prepared_df["hours_numpy"]
    )

    feature_columns = FEATURE_COLUMNS + ["total_study_hours"]
    return prepared_df[feature_columns], prepared_df[target_column]


def normalize_features(X: pd.DataFrame) -> pd.DataFrame:
    normalized = X.copy()
    for column in normalized.columns:
        std = float(normalized[column].std())
        if std == 0.0:
            std = 1.0
        normalized[column] = (
            normalized[column] - float(normalized[column].mean())
        ) / std
    return normalized


def make_dataloader(X: pd.DataFrame, y: pd.Series, batch_size: int) -> DataLoader:
    features = torch.tensor(X.to_numpy(), dtype=torch.float32)
    targets = torch.tensor(y.to_numpy(), dtype=torch.float32).reshape(-1, 1)
    dataset = TensorDataset(features, targets)
    return DataLoader(dataset, batch_size=batch_size, shuffle=True)


def build_model(input_dim: int) -> nn.Module:
    return nn.Sequential(
        nn.Linear(input_dim, 16),
        nn.ReLU(),
        nn.Linear(16, 1),
    )


def train_model(
    model: nn.Module, dataloader: DataLoader, config: TrainingConfig
) -> list[float]:
    optimizer = torch.optim.Adam(model.parameters(), lr=config.learning_rate)
    loss_fn = nn.MSELoss()
    loss_history: list[float] = []

    for _ in range(config.epochs):
        epoch_loss = 0.0
        for X_batch, y_batch in dataloader:
            predictions = model(X_batch)
            loss = loss_fn(predictions, y_batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            epoch_loss += float(loss.item())
        loss_history.append(epoch_loss / len(dataloader))

    return loss_history


def evaluate_model(model: nn.Module, X: pd.DataFrame, y: pd.Series) -> float:
    features = torch.tensor(X.to_numpy(), dtype=torch.float32)
    targets = torch.tensor(y.to_numpy(), dtype=torch.float32).reshape(-1, 1)
    with torch.no_grad():
        predictions = model(features)
    mae = torch.mean(torch.abs(predictions - targets))
    return float(mae.item())


def main() -> None:
    config = TrainingConfig(
        data_path=Path(__file__).resolve().parents[2]
        / "data"
        / "student_dev_ai_practice.csv"
    )
    df = load_data(config.data_path)
    X, y = prepare_features(df, config.target_column)
    X_normalized = normalize_features(X)
    dataloader = make_dataloader(X_normalized, y, config.batch_size)

    model = build_model(X_normalized.shape[1])
    loss_history = train_model(model, dataloader, config)
    mae = evaluate_model(model, X_normalized, y)

    print("feature shape:", X_normalized.shape)
    print("final training loss:", round(loss_history[-1], 4))
    print("training MAE:", round(mae, 4))


if __name__ == "__main__":
    main()
