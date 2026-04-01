import argparse
import os
from dataclasses import dataclass
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parent / ".mplconfig"))

from data_utils import load_dataset, prepare_features
from model_utils import infer_problem_type, train_and_evaluate
from plot_utils import save_target_plot


@dataclass(frozen=True)
class AppConfig:
    csv_path: Path
    target_column: str


def parse_args() -> AppConfig:
    default_path = Path(__file__).resolve().parents[2] / "data" / "student_dev_ai_practice.csv"
    parser = argparse.ArgumentParser(description="Run a small engineering-style ML baseline.")
    parser.add_argument("csv_path", nargs="?", default=default_path, type=Path)
    parser.add_argument("--target", default="test_score")
    args = parser.parse_args()
    return AppConfig(csv_path=args.csv_path, target_column=args.target)


def main() -> None:
    config = parse_args()
    dataframe = load_dataset(config.csv_path)
    prepared = prepare_features(dataframe, config.target_column)
    problem_type = infer_problem_type(config.target_column)
    result = train_and_evaluate(prepared.features, prepared.target, problem_type)
    outputs_dir = Path(__file__).resolve().parent / "outputs"
    plot_path = save_target_plot(dataframe, config.target_column, outputs_dir)

    print("rows:", len(dataframe))
    print("features:", prepared.features.shape[1])
    print("problem type:", result.problem_type)
    print(f"test {result.metric_name}:", round(result.metric_value, 3))
    print("plot saved to:", plot_path)


if __name__ == "__main__":
    main()
