# Day 10 - Clean Missing Values

Write `clean_missing_values.py` and practice simple cleaning decisions.

## Tasks

- Count missing values per column.
- Fill numeric missing values with the column mean.
- Verify that the cleaned DataFrame has no missing values left.
- Write 2 sentences explaining why mean filling was acceptable here.
- Write a `fill_numeric_missing(df)` helper that returns a cleaned copy instead of mutating in place.
- Add one assertion or explicit check that verifies no numeric missing values remain.
- Write one note about when mean filling would be a bad choice.

## Stronger Python Goal

Practice writing pure-ish transformation functions: input DataFrame in, cleaned DataFrame out.

## Suggested Output Files

- one `.py` file or notebook scratch file created from your IDE
- optional `.png` plots for visualization days
- a short text summary in comments or markdown

## Data

- Week 1 mainly uses `data/tiny_scores.csv`
- Week 2 and Week 3 mainly use `data/student_dev_ai_practice.csv`

## Git Checkpoint

Commit before and after cleaning if you want a clear history of the change.

## Colab Note

If a library is missing on your machine, keep writing code locally in your IDE,
commit the code to git, then run the training or notebook part in Google Colab.
