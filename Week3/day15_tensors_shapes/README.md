# Day 15 - Tensors and Shapes

Write `tensor_basics.py` or use Colab after coding the file in your IDE.

## Prerequisites

Before this day, you should already understand:

- what a feature matrix is
- what a target column is
- how train/test splits and normalization work
- how to save preprocessing logic in helper functions

If that still feels shaky, go back to `Week2/WEEK2_TO_WEEK3_BRIDGE.md` first.

## Task Levels

### Level 1 - Easy

- Convert your normalized feature DataFrames to float tensors.
- Convert your target columns to tensors with shape `(n, 1)`.
- Print all shapes.

### Level 2 - Core

- Write one sentence explaining what `(n_samples, n_features)` means.
- Create one helper that converts pandas or NumPy inputs into tensors.
- Add assertions for expected shapes.

### Level 3 - Hard

- Write one small debug helper that prints tensor dtype, shape, and device.
- Compare the shape of one pandas object, one NumPy array, and one tensor in your notes.
- Make your tensor conversion code reusable for both regression and classification.

## Stronger Python Goal

Start making your tensor code self-checking instead of trusting every conversion blindly.

## Suggested Output Files

- one `.py` file or notebook scratch file created from your IDE
- optional `.png` plots for visualization days
- a short text summary in comments or markdown

## Data

- Week 1 mainly uses `data/tiny_scores.csv`
- Week 2 and Week 3 mainly use `data/student_dev_ai_practice.csv`

## Git Checkpoint

Commit your local code, then run the same file or notebook section in Colab if PyTorch is not installed locally.

## Colab Note

If a library is missing on your machine, keep writing code locally in your IDE,
commit the code to git, then run the training or notebook part in Google Colab.
