import unittest

import pandas as pd

from templates.test_ready_project.data_utils import prepare_features_and_target


class TestDataUtils(unittest.TestCase):
    def test_prepare_features_and_target_fills_numeric_missing_values(self):
        df = pd.DataFrame(
            {
                "hours_python": [1.0, None, 3.0],
                "projects_completed": [0, 1, 2],
                "test_score": [50.0, 60.0, 70.0],
            }
        )

        X, y = prepare_features_and_target(df, "test_score")

        self.assertEqual(y.tolist(), [50.0, 60.0, 70.0])
        self.assertFalse(X.isna().any().any())
        self.assertIn("hours_python", X.columns)


if __name__ == "__main__":
    unittest.main()
