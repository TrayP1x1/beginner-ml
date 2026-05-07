import csv
from pathlib import Path


def csv_reader(path, r: int = 1):
    rows = load_rows(path)

    if not rows:
        print("The file has no student rows.")
        return

    print(f"The column names are: {list(rows[0].keys())}")

    for row in rows[:r]:
        print(row)

    total_score = sum(row["python_score"] for row in rows)
    amount_of_students = len(rows)

    print(f"The average python score is {total_score / amount_of_students:.2f}")
    print(f"The amount of students is {amount_of_students}")


def csv_writer(path):
    with path.open("w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([])


def load_rows(path) -> list[dict[str, str | float]]:
    rows = []

    with path.open("r", newline="") as file:
        reader = csv.DictReader(file)
        numeric_columns = ["python_score", "numpy_score"]
        fieldnames = reader.fieldnames or []

        missing_columns = [
            column for column in numeric_columns if column not in fieldnames
        ]
        if missing_columns:
            missing = ", ".join(missing_columns)
            raise KeyError(f"Expected column(s) missing from CSV: {missing}")

        for row in reader:
            for column in numeric_columns:
                try:
                    row[column] = float(row[column])
                except (ValueError, TypeError):
                    row[column] = 0.0

            rows.append(row)

    return rows


def main():
    # Path(__file__) is current file, .resolve() is hard file .parents[]
    tiny_scores_path = Path(__file__).resolve().parents[2] / "data" / "tiny_scores.csv"
    csv_reader(tiny_scores_path, 3)


if __name__ == "__main__":
    main()
