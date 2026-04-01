# Day 7 - Week 1 Mini Project

Create `week1_mini_project.py` and solve a full CSV task without pandas.
This day also introduces a simple class and the pattern of running everything from `main()`.

## Tasks

- Read `data/tiny_scores.csv`.
- Print the header and all rows.
- Compute the average score for both numeric columns.
- Print a short text summary of what you found.
- Put the repeated logic into helper functions such as `load_scores()` and `print_summary()`.
- Create one small class such as `ScoreRow` or `StudentSummary` to hold related values from one row.
- Add a `main()` function that calls your helpers.
- Run the script with:
  `if __name__ == "__main__":`
  `    main()`

## Why This Matters

If your scripts keep growing, you do not want all logic mixed together at the top level.
A beginner-friendly structure is:

- imports
- one or two small classes when related data belongs together
- helper functions
- `main()`
- `if __name__ == "__main__": main()`

You will use this same idea later when your data-loading, cleaning, plotting, and training code becomes larger.

## Suggested Shape

Your file can look roughly like this:

```python
import csv
from pathlib import Path


class ScoreRow:
    def __init__(self, name, math_score, python_score):
        self.name = name
        self.math_score = float(math_score)
        self.python_score = float(python_score)

    def average_score(self):
        return (self.math_score + self.python_score) / 2


def load_scores(path):
    ...


def print_summary(rows):
    ...


def main():
    data_path = Path("data/tiny_scores.csv")
    rows = load_scores(data_path)
    print_summary(rows)


if __name__ == "__main__":
    main()
```

## Suggested Output Files

- one `.py` file or notebook scratch file created from your IDE
- optional `.png` plots for visualization days
- a short text summary in comments or markdown

## Data

- Week 1 mainly uses `data/tiny_scores.csv`
- Week 2 and Week 3 mainly use `data/student_dev_ai_practice.csv`

## Git Checkpoint

Push your work to GitHub and make sure you can pull it again from another machine or Colab.

## Colab Note

If a library is missing on your machine, keep writing code locally in your IDE,
commit the code to git, then run the training or notebook part in Google Colab.
