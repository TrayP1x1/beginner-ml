# Day 12 - Feature Engineering

Write `feature_engineering.py` and create stronger inputs for a model.

## Prerequisites

Before this day, you should already be comfortable with:

- defining and calling small functions
- loading a CSV with pandas
- selecting columns and creating new columns

## Task Levels

### Level 1 - Easy

- Add `total_study_hours = hours_python + hours_numpy`.
- Compute the correlation matrix.

### Level 2 - Core

- Add `projects_per_test = projects_completed / (practice_tests + 1)`.
- Write 3 short observations about which features look most useful.
- Create a function `add_engineered_features(df)` that returns a new DataFrame.

### Level 3 - Hard

- Keep raw-column assumptions documented in a short docstring.
- Add one guard against division-by-zero or missing required columns.
- Write your transformation code so it is easy to reuse in later modeling days.

## Stronger Python Goal

Make your transformation steps explicit and reviewable.

## Suggested Output Files

- one `.py` file or notebook scratch file created from your IDE
- optional `.png` plots for visualization days
- a short text summary in comments or markdown

## Data

- Week 1 mainly uses `data/tiny_scores.csv`
- Week 2 and Week 3 mainly use `data/student_dev_ai_practice.csv`

## Git Checkpoint

Use git to compare your new version with the previous one by running `git diff`.

## Colab Note

If a library is missing on your machine, keep writing code locally in your IDE,
commit the code to git, then run the training or notebook part in Google Colab.
