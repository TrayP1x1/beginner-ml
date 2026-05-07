from pathlib import Path

import pandas as pd


def load_dataset(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"Missing dataset: {csv_path}")
    return pd.read_csv(csv_path)


def inspect_dataframe(df: pd.DataFrame) -> dict[str, object]:
    return {
        "row_count": len(df),
        "column_count": len(df.columns),
        "numeric_columns": df.select_dtypes(include="number").columns.tolist(),
        "missing_counts": {
            column: int(count) for column, count in df.isna().sum().items()
        },
    }


def print_inspection_report(df: pd.DataFrame) -> None:
    summary = inspect_dataframe(df)
    print("Head:")
    print(df.head())
    print()
    print("Describe:")
    print(df.describe(include="all"))
    print()
    print("Summary:", summary)


def main() -> None:
    data_path = (
        Path(__file__).resolve().parents[2] / "data" / "student_dev_ai_practice.csv"
    )
    dataframe = load_dataset(data_path)
    print_inspection_report(dataframe)


if __name__ == "__main__":
    main()
