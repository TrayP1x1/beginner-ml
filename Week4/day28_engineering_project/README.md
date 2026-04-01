# Day 28 Example Project

This folder is a small example of the final Week 4 engineering shape.

## Layout

```text
day28_engineering_project/
  main.py
  data_utils.py
  model_utils.py
  plot_utils.py
  outputs/
  tests/
  README.md
```

## What It Demonstrates

- one obvious entry point from `main.py`
- CSV loading and validation
- feature preparation separated from model code
- one saved plot in `outputs/`
- a small automated test suite

## Run It

From the repo root:

```bash
.venv/bin/python Week4/day28_engineering_project/main.py --target test_score
```

Run tests with:

```bash
.venv/bin/python -m unittest discover Week4/day28_engineering_project/tests
```
