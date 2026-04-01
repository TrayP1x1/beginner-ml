import unittest

import pandas as pd

from templates.test_ready_project.model_utils import (
    EvaluationResult,
    evaluate_model,
    infer_problem_type,
    split_data,
)


class DummyClassificationModel:
    def predict_proba(self, X: pd.DataFrame):
        return [[0.2, 0.8] for _ in range(len(X))]


class DummyRegressionModel:
    def predict(self, X: pd.DataFrame):
        return [10.0 for _ in range(len(X))]


class TestModelUtils(unittest.TestCase):
    def test_infer_problem_type_for_classification_target(self) -> None:
        self.assertEqual(infer_problem_type("passed_test"), "classification")

    def test_infer_problem_type_for_regression_target(self) -> None:
        self.assertEqual(infer_problem_type("test_score"), "regression")

    def test_split_data_rejects_invalid_test_size(self) -> None:
        X = pd.DataFrame({"feature": [1, 2, 3]})
        y = pd.Series([0, 1, 0])

        with self.assertRaises(ValueError):
            split_data(X, y, problem_type="classification", test_size=1.0, random_state=42)

    def test_evaluate_model_returns_accuracy_for_classification(self) -> None:
        X_test = pd.DataFrame({"feature": [1, 2]})
        y_test = pd.Series([1, 1])

        result = evaluate_model(
            DummyClassificationModel(),
            X_test,
            y_test,
            problem_type="classification",
        )

        self.assertIsInstance(result, EvaluationResult)
        self.assertEqual(result.metric_name, "accuracy")
        self.assertEqual(result.metric_value, 1.0)

    def test_evaluate_model_returns_mae_for_regression(self) -> None:
        X_test = pd.DataFrame({"feature": [1, 2]})
        y_test = pd.Series([8.0, 12.0])

        result = evaluate_model(
            DummyRegressionModel(),
            X_test,
            y_test,
            problem_type="regression",
        )

        self.assertEqual(result.metric_name, "mae")
        self.assertEqual(result.metric_value, 2.0)


if __name__ == "__main__":
    unittest.main()
