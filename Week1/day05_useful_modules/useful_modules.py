import math
from pathlib import Path
import csv
import random
import statistics

def sample_three_numbers(list_of_numbers: list[int|float]) -> list[int|float]:
    return random.sample(list_of_numbers, k=3)

def compute_mean(list_of_numbers: list[int|float]) -> float: 
    return statistics.mean(list_of_numbers)

def return_numeric_values(path: Path, numeric_column_name: str) -> list[float]:
    if not numeric_column_name:
        raise ValueError("numeric_column_name is empty")

    with path.open("r", newline="") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames

        if not fieldnames:
            raise ValueError(f"{path.name} is missing a header row")

        if numeric_column_name not in fieldnames:
            raise ValueError(f"{numeric_column_name} is not in {path.name}")

        list_of_numbers = []
        for row in reader:
            # Re-raise with column context so bad CSV values are easier to debug.
            try:
                list_of_numbers.append(float(row[numeric_column_name]))
            except ValueError as error:
                raise ValueError(
                    f"Could not convert {row[numeric_column_name]!r} in "
                    f"{numeric_column_name} to float"
                ) from error

    return list_of_numbers


def show_field_names(path: Path) -> list[str]:
    with path.open("r", newline="") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames

        if not fieldnames:
            raise ValueError(f"{path.name} is missing a header row")

        return fieldnames


def main() -> None:
    path = Path(__file__).resolve().parents[2] / "data" / "tiny_scores.csv"

    print(math.sqrt(81))
    print(f'{math.log(27, 3)}\n\n')

    try:
        # Loop through each CSV column and only print the numeric ones.
        for field_name in show_field_names(path):
            try:
                print(f"A sample of 3 numbers from {field_name} is\n{sample_three_numbers(return_numeric_values(path, field_name))}")
                print(f"The mean of {field_name} is {compute_mean(return_numeric_values(path, field_name)):.2f}")
            except ValueError as error:
                # print(error)
                continue
    except FileNotFoundError as error:
        print(error)


if __name__ == "__main__":
    main()
