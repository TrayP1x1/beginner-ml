# Test-Ready Project Template

This template is here to help you practice the shape of a clean coding-test solution after the 3-week Python ramp.

- load data from a CSV
- inspect it quickly
- validate inputs and clean missing values
- train one baseline model
- report one metric
- run everything from `main.py`
- accept command-line inputs with `argparse`
- keep a few automated tests

## Files

- `main.py`: the entry point and CLI parsing
- `data_utils.py`: loading, validation, summary, and feature preparation
- `model_utils.py`: problem inference, splitting, training, and evaluation
- `plot_utils.py`: quick plots saved to disk
- `tests/`: `unittest` coverage for helpers and failure cases

## Recommended Submission Structure

For a take-home test, a very strong default layout is:

```text
project/
  main.py
  data_utils.py
  model_utils.py
  plot_utils.py
  outputs/
  tests/
  README.md
```

Use each part like this:

- `main.py`: one obvious entry point the reviewer can run
- `data_utils.py`: CSV loading, validation, cleaning, and feature preparation
- `model_utils.py`: model training and evaluation
- `plot_utils.py`: charts saved to disk
- `outputs/`: generated plots or other run artifacts
- `tests/`: a few focused automated tests
- `README.md`: how to run the project, what the target is, and what you chose to do

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
.venv/bin/python templates/test_ready_project/main.py data/student_dev_ai_practice.csv --target passed_test --no-plots
```

Run the tests with:

```bash
.venv/bin/python -m unittest discover templates/test_ready_project/tests
```

By default it trains on `data/student_dev_ai_practice.csv`.
You can also pass values from the terminal with named flags.
Useful targets include:

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
One simple config class plus a few focused helper modules is already a strong step toward cleaner Python.
