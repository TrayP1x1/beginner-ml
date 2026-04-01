import unittest

import pandas as pd

from templates.test_ready_project.data_utils import (
    build_dataset_summary,
    fill_numeric_missing_values,
    prepare_features_and_target,
)


class TestDataUtils(unittest.TestCase):
    def test_fill_numeric_missing_values_returns_clean_copy(self) -> None:
        df = pd.DataFrame(
            {
                "hours_python": [1.0, None, 3.0],
                "projects_completed": [0, 1, 2],
                "test_score": [50.0, 60.0, 70.0],
            }
        )

        cleaned_df = fill_numeric_missing_values(df)

        self.assertTrue(df["hours_python"].isna().any())
        self.assertFalse(cleaned_df.isna().any().any())

    def test_prepare_features_and_target_fills_numeric_missing_values(self) -> None:
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

    def test_build_dataset_summary_raises_for_missing_target(self) -> None:
        df = pd.DataFrame({"hours_python": [1.0, 2.0]})

        with self.assertRaises(ValueError):
            build_dataset_summary(df, "test_score")


if __name__ == "__main__":
    unittest.main()
