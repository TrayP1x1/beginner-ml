# Day 13 - Split and Normalize

Write `split_and_normalize.py` and prepare features for modeling.

## Prerequisites

Before this day, you should already be comfortable with:

- selecting feature columns and one target column
- writing small helpers that return cleaned data
- basic DataFrame operations with pandas

## Task Levels

### Level 1 - Easy

- Shuffle the rows.
- Split into train, validation, and test sets.
- Print the shapes of all three splits.

### Level 2 - Core

- Normalize the feature columns using training-set statistics only.
- Write separate helpers for splitting and normalization.

### Level 3 - Hard

- Store normalization statistics in a dictionary or small dataclass.
- Add one note explaining why using validation or test statistics would be leakage.
- Save your final normalized outputs in a shape that is easy to reuse on Day 15.

## Stronger Python Goal

This is the day to practice pipeline thinking: fit on train, apply everywhere else.

## Suggested Output Files

- one `.py` file or notebook scratch file created from your IDE
- optional `.png` plots for visualization days
- a short text summary in comments or markdown

## Data

- Week 1 mainly uses `data/tiny_scores.csv`
- Week 2 and Week 3 mainly use `data/student_dev_ai_practice.csv`

## Git Checkpoint

Commit after you verify the split works and keep the code very readable.

## Colab Note

If a library is missing on your machine, keep writing code locally in your IDE,
commit the code to git, then run the training or notebook part in Google Colab.
