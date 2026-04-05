import csv
from pathlib import Path


def csv_reader(path, r: int = 1):

    with path.open("r", newline="") as file:
        reader = csv.DictReader(file)
        print(f"The column names are: {reader.fieldnames}")

        total_score = 0
        amount_of_students = 0

        for i, row in enumerate(reader):
            if i < r:
                print(row)

            total_score += float(row["python_score"])
            amount_of_students += 1

        if amount_of_students > 0:
            print(f"The average python score is {total_score/amount_of_students:.2f}")
        else:
            print("The list has no python scores")

        print(f"The amount of students is {amount_of_students}")


def csv_writeer():
    tiny_scores_path = Path(__file__).resolve().parents[2] / "data" / "tiny_scores.csv"

    with tiny_scores_path.open("w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([])


def main():
    # Path(__file__) is current file, .resolve() is hard file .parents[]
    tiny_scores_path = Path(__file__).resolve().parents[2] / "data" / "tiny_scores.csv"
    csv_reader(tiny_scores_path, 3)


if __name__ == "__main__":
    main()
