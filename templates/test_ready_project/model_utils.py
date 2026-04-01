from typing import Literal

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, mean_absolute_error
from sklearn.model_selection import train_test_split


ProblemType = Literal["regression", "classification"]


def infer_problem_type(target_column: str) -> ProblemType:
    if target_column == "passed_test":
        return "classification"
    return "regression"


def split_data(X, y, test_size: float, random_state: int):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def train_model(X_train, y_train, problem_type: ProblemType):
    if problem_type == "classification":
        model = LogisticRegression(max_iter=1000)
    else:
        model = LinearRegression()

    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test, problem_type: ProblemType) -> float:
    predictions = model.predict(X_test)

    if problem_type == "classification":
        predicted_labels = (predictions >= 0.5).astype(int)
        return accuracy_score(y_test, predicted_labels)

    return mean_absolute_error(y_test, predictions)
