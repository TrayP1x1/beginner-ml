# Day 17 - Binary Classification

Train a classifier to predict `passed_test`.
When the synthetic dataset feels manageable, repeat the same workflow on `data/kaggle/titanic.csv`.

## Tasks

- Use `nn.BCEWithLogitsLoss()`.
- Train for multiple epochs.
- Convert logits to probabilities with `torch.sigmoid`.
- Compute test accuracy.

## Suggested Output Files

- one `.py` file or notebook scratch file created from your IDE
- optional `.png` plots for visualization days
- a short text summary in comments or markdown

## Data

- Week 1 mainly uses `data/tiny_scores.csv`
- Week 2 and Week 3 mainly use `data/student_dev_ai_practice.csv`
- Best real classification follow-up: `data/kaggle/titanic.csv`
- Bonus later: `data/kaggle/iris.csv`

## Git Checkpoint

Push your code once the pipeline works end to end, even if the accuracy is not perfect yet.

## Colab Note

If a library is missing on your machine, keep writing code locally in your IDE,
commit the code to git, then run the training or notebook part in Google Colab.
