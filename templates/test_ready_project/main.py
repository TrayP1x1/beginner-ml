import os
import sys
from dataclasses import dataclass
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parent / ".mplconfig"))

from data_utils import load_dataset, prepare_features_and_target, print_dataset_summary
from model_utils import evaluate_model, infer_problem_type, split_data, train_model
from plot_utils import save_quick_plots


@dataclass
class TrainingConfig:
    data_path: Path
    target_column: str
    test_size: float = 0.2
    random_state: int = 42


def run_pipeline(config: TrainingConfig) -> None:
    df = load_dataset(config.data_path)
    print_dataset_summary(df, config.target_column)

    plots_dir = Path(__file__).resolve().parent / "outputs"
    save_quick_plots(df, config.target_column, plots_dir)

    X, y = prepare_features_and_target(df, config.target_column)
    problem_type = infer_problem_type(config.target_column)

    X_train, X_test, y_train, y_test = split_data(
        X, y, test_size=config.test_size, random_state=config.random_state
    )
    model = train_model(X_train, y_train, problem_type)
    metric_value = evaluate_model(model, X_test, y_test, problem_type)

    print()
    print("problem type:", problem_type)
    if problem_type == "classification":
        print("test accuracy:", round(metric_value, 3))
    else:
        print("test MAE:", round(metric_value, 3))
    print("plots saved to:", plots_dir)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    default_data_path = repo_root / "data" / "student_dev_ai_practice.csv"
    default_target_column = "test_score"

    args = sys.argv[1:]
    data_path = Path(args[0]) if len(args) >= 1 else default_data_path
    target_column = args[1] if len(args) >= 2 else default_target_column

    if len(args) > 2:
        print("Usage: python main.py [csv_path] [target_column]")
        sys.exit(1)

    config = TrainingConfig(data_path=data_path, target_column=target_column)
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
