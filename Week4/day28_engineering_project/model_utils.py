from dataclasses import dataclass
from typing import Literal

import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, mean_absolute_error
from sklearn.model_selection import train_test_split


ProblemType = Literal["regression", "classification"]


@dataclass(frozen=True)
class EvaluationResult:
    problem_type: ProblemType
    metric_name: str
    metric_value: float


def infer_problem_type(target_column: str) -> ProblemType:
    if target_column.strip().lower() in {"passed_test", "survived"}:
        return "classification"
    return "regression"


def train_and_evaluate(
    features: pd.DataFrame, target: pd.Series, problem_type: ProblemType
) -> EvaluationResult:
    X_train, X_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=0.2,
        random_state=42,
        stratify=target if problem_type == "classification" else None,
    )

    if problem_type == "classification":
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        return EvaluationResult(problem_type, "accuracy", float(accuracy))

    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    return EvaluationResult(problem_type, "mae", float(mae))
