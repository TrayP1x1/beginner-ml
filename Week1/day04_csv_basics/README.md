# Day 4 - CSV Basics

Work with `data/tiny_scores.csv` using the built-in `csv` module and write `read_tiny_scores.py`.

## Tasks

- Read the file and print the header.
- Print the first 3 rows.
- Compute the average of `python_score` manually.
- Count how many students are in the file.
- Create a helper function `load_rows(path)` that returns parsed rows.
- Convert numeric columns safely instead of leaving them as strings.
- Raise a helpful error if an expected column is missing.
- Use `Path` from `pathlib` for the file path.

## Stronger Python Goal

Practice separating:

- file loading
- row parsing
- summary computation
- output formatting

## Suggested Output Files

- one `.py` file or notebook scratch file created from your IDE
- optional `.png` plots for visualization days
- a short text summary in comments or markdown

## Data

- Week 1 mainly uses `data/tiny_scores.csv`
- Week 2 and Week 3 mainly use `data/student_dev_ai_practice.csv`

## Git Checkpoint

After your code works, run `git status` and confirm only your intended files changed.

## Colab Note

If a library is missing on your machine, keep writing code locally in your IDE,
commit the code to git, then run the training or notebook part in Google Colab.
