import sys
import unittest
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from model_utils import infer_problem_type, train_and_evaluate


class TestModelUtils(unittest.TestCase):
    def test_infer_problem_type_detects_classification_targets(self) -> None:
        self.assertEqual(infer_problem_type("passed_test"), "classification")

    def test_infer_problem_type_defaults_to_regression(self) -> None:
        self.assertEqual(infer_problem_type("test_score"), "regression")

    def test_train_and_evaluate_returns_metric_name(self) -> None:
        features = pd.DataFrame({"hours_python": [1, 2, 3, 4, 5, 6]})
        target = pd.Series([50.0, 60.0, 70.0, 80.0, 90.0, 100.0])

        result = train_and_evaluate(features, target, "regression")

        self.assertEqual(result.metric_name, "mae")
        self.assertGreaterEqual(result.metric_value, 0.0)


if __name__ == "__main__":
    unittest.main()
