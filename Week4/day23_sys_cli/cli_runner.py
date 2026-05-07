import argparse
from pathlib import Path

import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect a CSV file from the command line."
    )
    default_path = (
        Path(__file__).resolve().parents[2] / "data" / "student_dev_ai_practice.csv"
    )
    parser.add_argument("csv_path", nargs="?", default=default_path, type=Path)
    parser.add_argument("--target", default="test_score")
    parser.add_argument(
        "--head", default=5, type=int, help="Number of rows to preview."
    )
    return parser.parse_args()


def load_dataset(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    return pd.read_csv(csv_path)


def main() -> None:
    args = parse_args()
    dataframe = load_dataset(args.csv_path)

    if args.target not in dataframe.columns:
        raise ValueError(f"Target column '{args.target}' not found.")

    print("shape:", dataframe.shape)
    print("target column:", args.target)
    print("preview:")
    print(dataframe.head(args.head))


if __name__ == "__main__":
    main()
