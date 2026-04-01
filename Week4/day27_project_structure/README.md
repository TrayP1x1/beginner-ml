# Day 27 - Project Structure and `main.py`

Practice building a project that another person can run in one command.

## Tasks

- Create or reuse `main.py`.
- Keep imports at the top.
- Keep config, helpers, and model code separated.
- Make sure `main.py` calls a `main()` function.
- End with:

```python
if __name__ == "__main__":
    main()
```

## Recommended Shape

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

## What Each File Is For

- `main.py`: one command entry point for the full workflow
- `data_utils.py`: loading, validation, cleaning, and feature prep
- `model_utils.py`: training and evaluation logic
- `plot_utils.py`: saved charts and visual diagnostics
- `outputs/`: generated plots or reports
- `tests/`: a few automated checks for helpers
- `README.md`: setup, run command, chosen target, and short explanation

## Stronger Python Goal

Think like someone packaging work for another developer:

- obvious entry point
- limited top-level side effects
- clear module responsibility
- imports that make sense from the repo root

## Why This Matters

This is the structure that helps you most in a timed test.
It is simple, readable, and easy to explain aloud.
