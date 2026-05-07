from dataclasses import dataclass
from typing import Any, Literal

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, mean_absolute_error
from sklearn.model_selection import train_test_split

ProblemType = Literal["regression", "classification"]

CLASSIFICATION_TARGETS = {"passed_test", "survived", "target", "label"}


@dataclass(frozen=True)
class EvaluationResult:
    metric_name: str
    metric_value: float


def infer_problem_type(target_column: str) -> ProblemType:
    normalized_target = target_column.strip().lower()
    if normalized_target in CLASSIFICATION_TARGETS:
        return "classification"
    return "regression"


def split_data(
    X: pd.DataFrame,
    y: pd.Series,
    problem_type: ProblemType,
    test_size: float,
    random_state: int,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    if not 0 < test_size < 1:
        raise ValueError("test_size must be between 0 and 1.")

    stratify = y if problem_type == "classification" else None
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=stratify,
    )


def create_model(problem_type: ProblemType) -> Any:
    if problem_type == "classification":
        return LogisticRegression(max_iter=1000)
    return LinearRegression()


def train_model(
    X_train: pd.DataFrame, y_train: pd.Series, problem_type: ProblemType
) -> Any:
    model = create_model(problem_type)
    model.fit(X_train, y_train)
    return model


def predict_probabilities(model: Any, X_test: pd.DataFrame) -> pd.Series:
    probability_matrix = np.asarray(model.predict_proba(X_test))
    probabilities = probability_matrix[:, 1]
    return pd.Series(probabilities, index=X_test.index)


def evaluate_model(
    model: Any,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    problem_type: ProblemType,
    threshold: float = 0.5,
) -> EvaluationResult:
    if problem_type == "classification":
        predicted_probabilities = predict_probabilities(model, X_test)
        predicted_labels = (predicted_probabilities >= threshold).astype(int)
        accuracy = accuracy_score(y_test, predicted_labels)
        return EvaluationResult(metric_name="accuracy", metric_value=float(accuracy))

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    return EvaluationResult(metric_name="mae", metric_value=float(mae))
