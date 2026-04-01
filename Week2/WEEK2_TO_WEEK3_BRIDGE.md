# Week 2 To Week 3 Bridge

This guide exists to prevent the Week 2 to Week 3 jump from feeling random.

The idea is simple:

1. Week 2 teaches you how to build a clean feature matrix and target column.
2. The bridge teaches you how those become arrays and tensors.
3. Week 3 teaches you how a model consumes those tensors.

## What You Should Already Know Before Day 15

You should already be able to explain:

- what `X` is
- what `y` is
- which columns are features and which column is the target
- why you split data before evaluating a model
- why normalization should be fit on the training set only
- what shape your final feature table has

If you cannot explain those yet, do not jump straight into PyTorch.

## The Bridge Mental Model

Use this sequence:

1. `pandas.DataFrame`
2. `NumPy array`
3. `torch.Tensor`
4. model predictions
5. loss
6. optimizer update

That means the learner should not see tensors as magic.
They are just the next representation of the same organized data.

## Bridge Tasks

### Level 1 - Easy

- Load `student_dev_ai_practice.csv`.
- Select feature columns into `X`.
- Select one target column into `y`.
- Print `X.shape` and `y.shape`.

### Level 2 - Core

- Convert `X` to a NumPy array and print its shape.
- Convert `y` to a NumPy array and reshape it to `(n, 1)`.
- Normalize `X` using training-set statistics.
- Explain why `X` is 2D and `y` is often reshaped to 2D.

### Level 3 - Hard

- Convert the NumPy arrays to `torch.float32` tensors.
- Add assertions for expected dimensions.
- Write one helper that converts a DataFrame and Series into model-ready tensors.
- Write one note explaining how this connects directly to Day 16 training.

## Recommended Starter File

Use:

- `Week2/day14_week2_project/week2_to_week3_bridge.py`

or build your own file with the same goal.

## Why This Matters

Most beginners do not actually struggle with the math first.
They struggle with data representation:

- DataFrame vs array vs tensor
- shape mistakes
- target shape mistakes
- forgetting what was normalized and when

If this bridge feels clear, the Week 3 modeling work becomes much more logical.
