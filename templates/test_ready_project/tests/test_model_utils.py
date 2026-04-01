import unittest

from templates.test_ready_project.model_utils import infer_problem_type


class TestModelUtils(unittest.TestCase):
    def test_infer_problem_type_for_classification_target(self):
        self.assertEqual(infer_problem_type("passed_test"), "classification")

    def test_infer_problem_type_for_regression_target(self):
        self.assertEqual(infer_problem_type("test_score"), "regression")


if __name__ == "__main__":
    unittest.main()
