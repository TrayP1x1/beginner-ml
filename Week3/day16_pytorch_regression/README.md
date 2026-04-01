# Day 16 - PyTorch Regression

Train a small network to predict `test_score`.
When the synthetic dataset feels manageable, repeat the same workflow on `data/kaggle/housing_prices.csv`.

## Tasks

- Build a small `nn.Sequential` model.
- Use `nn.MSELoss()` and an optimizer such as Adam.
- Track train and validation loss for multiple epochs.
- Compute mean absolute error on the test set.

## Suggested Output Files

- one `.py` file or notebook scratch file created from your IDE
- optional `.png` plots for visualization days
- a short text summary in comments or markdown

## Data

- Week 1 mainly uses `data/tiny_scores.csv`
- Week 2 and Week 3 mainly use `data/student_dev_ai_practice.csv`
- Best real regression follow-up: `data/kaggle/housing_prices.csv`

## Git Checkpoint

Commit your model code before you start tuning hyperparameters so you can always go back to a clean baseline.

## Bonus Link

- `Bonus/bonus_least_squares_regression.md` is a useful least-squares regression warm-up before or after this day.

## Colab Note

If a library is missing on your machine, keep writing code locally in your IDE,
commit the code to git, then run the training or notebook part in Google Colab.
