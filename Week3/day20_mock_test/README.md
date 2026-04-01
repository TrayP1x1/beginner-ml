# Day 20 - Mock Test

Pretend you have 60 to 90 minutes and solve the task like a real test.

## Tasks

- Start from a blank file or notebook.
- Load the CSV and inspect it quickly.
- Make two plots.
- Train one simple model and report one metric.
- Keep the final version runnable from `main.py` or from a file with a `main()` entry point.
- After one run with the synthetic dataset, repeat the mock test with either `data/kaggle/housing_prices.csv` or `data/kaggle/titanic.csv`.
- Use helper functions from the start instead of writing everything inline first.
- Add at least one type hint to each top-level helper.
- Leave the code in a state that another person could review in five minutes.

## Mock-Test Rule

Pretend the reviewer will only run one command.
That means your code should have one obvious entry point and should not require running cells in a special order.

## Stronger Python Goal

The challenge is not only speed. It is writing clean code under time pressure.

## Suggested Output Files

- one `.py` file or notebook scratch file created from your IDE
- optional `.png` plots for visualization days
- a short text summary in comments or markdown

## Data

- Week 1 mainly uses `data/tiny_scores.csv`
- Week 2 and Week 3 mainly use `data/student_dev_ai_practice.csv`
- Best realistic mock-test choices: `data/kaggle/housing_prices.csv` and `data/kaggle/titanic.csv`

## Git Checkpoint

At the end, tag the commit mentally as a rehearsal: the goal is confidence and flow, not perfect code.

## Colab Note

If a library is missing on your machine, keep writing code locally in your IDE,
commit the code to git, then run the training or notebook part in Google Colab.
