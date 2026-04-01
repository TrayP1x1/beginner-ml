import argparse
import os
import sys
from dataclasses import dataclass
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parent / ".mplconfig"))

from data_utils import (
    build_dataset_summary,
    load_dataset,
    prepare_features_and_target,
    print_dataset_summary,
)
from model_utils import EvaluationResult, evaluate_model, infer_problem_type, split_data, train_model
from plot_utils import save_quick_plots


@dataclass(frozen=True)
class TrainingConfig:
    data_path: Path
    target_column: str
    test_size: float = 0.2
    random_state: int = 42
    save_plots: bool = True


def parse_args() -> TrainingConfig:
    repo_root = Path(__file__).resolve().parents[2]
    default_data_path = repo_root / "data" / "student_dev_ai_practice.csv"

    parser = argparse.ArgumentParser(
        description="Train a simple baseline model on a CSV dataset."
    )
    parser.add_argument("csv_path", nargs="?", default=default_data_path, type=Path)
    parser.add_argument("--target", default="test_score", help="Target column to predict.")
    parser.add_argument(
        "--test-size",
        default=0.2,
        type=float,
        help="Fraction of rows to reserve for the test set.",
    )
    parser.add_argument(
        "--random-state",
        default=42,
        type=int,
        help="Random seed used for train/test splitting.",
    )
    parser.add_argument(
        "--no-plots",
        action="store_true",
        help="Skip saving quick diagnostic plots.",
    )

    args = parser.parse_args()
    return TrainingConfig(
        data_path=args.csv_path,
        target_column=args.target,
        test_size=args.test_size,
        random_state=args.random_state,
        save_plots=not args.no_plots,
    )


def print_evaluation(problem_type: str, evaluation: EvaluationResult) -> None:
    print()
    print("problem type:", problem_type)
    print(f"test {evaluation.metric_name}:", round(evaluation.metric_value, 3))


def run_pipeline(config: TrainingConfig) -> EvaluationResult:
    df = load_dataset(config.data_path)
    summary = build_dataset_summary(df, config.target_column)
    print_dataset_summary(summary, df)

    if config.save_plots:
        plots_dir = Path(__file__).resolve().parent / "outputs"
        save_quick_plots(df, config.target_column, plots_dir)
        print("plots saved to:", plots_dir)

    X, y = prepare_features_and_target(df, config.target_column)
    problem_type = infer_problem_type(config.target_column)

    X_train, X_test, y_train, y_test = split_data(
        X,
        y,
        problem_type=problem_type,
        test_size=config.test_size,
        random_state=config.random_state,
    )
    model = train_model(X_train, y_train, problem_type)
    evaluation = evaluate_model(model, X_test, y_test, problem_type)
    print_evaluation(problem_type, evaluation)
    return evaluation


def main() -> None:
    config = parse_args()
    try:
        run_pipeline(config)
    except FileNotFoundError:
        print(f"Could not find CSV file: {config.data_path}")
        sys.exit(1)
    except ValueError as error:
        print(f"Configuration error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
