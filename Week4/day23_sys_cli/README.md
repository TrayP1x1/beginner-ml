# Day 23 - Command-Line Arguments With `sys`

Write `cli_runner.py` and practice passing values into a script from the terminal.

## Tasks

- Import `sys`.
- Read a CSV path from `sys.argv`.
- Read an optional target column from `sys.argv`.
- Print a usage message if the arguments are missing.
- Call a `main()` function that receives those values.

## Why This Matters

Many coding tests and real projects become easier to reuse when you can run:

```bash
python main.py data/student_dev_ai_practice.csv test_score
```

That is much cleaner than editing values manually every time.

## Stretch Goal

- If the user passes the wrong number of arguments, return a non-zero exit code with `sys.exit(1)`.
