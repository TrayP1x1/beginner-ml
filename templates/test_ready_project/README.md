# Test-Ready Project Template

This template is here to help you practice the exact shape of a coding test solution:

- load data from a CSV
- inspect it quickly
- clean simple missing values
- train one model
- report one metric
- run everything from `main.py`
- accept simple command-line inputs with `sys.argv`
- keep a few automated tests

## Files

- `main.py`: the entry point
- `data_utils.py`: loading, quick inspection, and feature preparation
- `model_utils.py`: model selection and evaluation
- `plot_utils.py`: quick plots saved to disk
- `tests/`: basic `unittest` coverage for helpers

## Why This Helps

When the test starts, you do not want to invent a project structure from scratch.
You want a small mental template:

1. read the CSV
2. inspect the columns
3. choose the target
4. build `X` and `y`
5. split the data
6. train a simple baseline model
7. print one metric
8. keep everything callable from `main()`

## How To Run

From the repo root:

```bash
.venv/bin/python templates/test_ready_project/main.py
```

Or with explicit arguments:

```bash
.venv/bin/python templates/test_ready_project/main.py data/student_dev_ai_practice.csv passed_test
```

Run the tests with:

```bash
.venv/bin/python -m unittest discover templates/test_ready_project/tests
```

By default it trains on `data/student_dev_ai_practice.csv`.
You can also pass values from the terminal.
The second argument is the target column:

- `"test_score"` for regression
- `"passed_test"` for classification

## Clean Code Pattern

Use this pattern in your own projects:

```python
imports

small config class

helper functions

main()

if __name__ == "__main__":
    main()
```

You do not need classes everywhere.
One simple class for configuration or for one row type is enough for beginner practice.
