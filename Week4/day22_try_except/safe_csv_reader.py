from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {"hours_python", "hours_numpy", "test_score"}


def load_scores(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    dataframe = pd.read_csv(csv_path)
    if dataframe.empty:
        raise ValueError("The CSV file is empty.")

    missing_columns = REQUIRED_COLUMNS.difference(dataframe.columns)
    if missing_columns:
        missing_display = ", ".join(sorted(missing_columns))
        raise KeyError(f"Missing required columns: {missing_display}")

    return dataframe


def summarize_scores(dataframe: pd.DataFrame) -> dict[str, float]:
    try:
        avg_python = float(dataframe["hours_python"].fillna(dataframe["hours_python"].median()).mean())
        avg_numpy = float(dataframe["hours_numpy"].fillna(dataframe["hours_numpy"].median()).mean())
        avg_test = float(dataframe["test_score"].mean())
    except ValueError as error:
        raise ValueError("Could not convert score values to numbers.") from error

    return {
        "avg_hours_python": round(avg_python, 2),
        "avg_hours_numpy": round(avg_numpy, 2),
        "avg_test_score": round(avg_test, 2),
    }


def main() -> None:
    data_path = Path(__file__).resolve().parents[2] / "data" / "student_dev_ai_practice.csv"

    try:
        dataframe = load_scores(data_path)
        summary = summarize_scores(dataframe)
        print("Summary:", summary)
    except FileNotFoundError as error:
        print(f"File error: {error}")
    except KeyError as error:
        print(f"Column error: {error}")
    except ValueError as error:
        print(f"Data error: {error}")
    finally:
        print("finished attempt")


if __name__ == "__main__":
    main()
