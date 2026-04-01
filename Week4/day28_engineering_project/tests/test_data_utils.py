import sys
import unittest
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from data_utils import clean_dataframe, prepare_features


class TestDataUtils(unittest.TestCase):
    def test_clean_dataframe_fills_numeric_missing_values(self) -> None:
        dataframe = pd.DataFrame(
            {
                "hours_python": [1.0, None, 3.0],
                "test_score": [60.0, 70.0, 80.0],
            }
        )

        cleaned = clean_dataframe(dataframe)

        self.assertFalse(cleaned.isna().any().any())
        self.assertTrue(dataframe["hours_python"].isna().any())

    def test_prepare_features_rejects_missing_target(self) -> None:
        dataframe = pd.DataFrame({"hours_python": [1.0, 2.0]})

        with self.assertRaises(ValueError):
            prepare_features(dataframe, "test_score")


if __name__ == "__main__":
    unittest.main()
