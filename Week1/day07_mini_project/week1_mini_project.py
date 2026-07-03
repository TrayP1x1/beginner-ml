import numpy as np
import csv


def print_headers(path):
    """
    Prints headers 
    """
    with path.open("r", newline="") as file:
        reader = csv.reader(file)
        print(next(reader))

