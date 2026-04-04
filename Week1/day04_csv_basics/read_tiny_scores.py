import csv
from pathlib import Path

def csv_reader(r:int= 1):
   
    tiny_scores_path = Path(__file__).resolve().parents[2] / "data" / "tiny_scores.csv"

    with tiny_scores_path.open("r", newline="") as file:
        reader = csv.DictReader(file)
        print(f'Headers: {reader.fieldnames}')

        for i, row in enumerate(reader):
            if i >= r:
                break
            print(row)















def calculator(number_1, number_2):
    return number_1 + number_2

print(calculator(8, 12))


























# def main():
#     csv_reader(3)

# if __name__ == '__main__':
#     main()


























