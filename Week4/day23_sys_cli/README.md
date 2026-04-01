# Day 23 - Command-Line Interfaces With `argparse`

Write `cli_runner.py` and practice passing values into a script from the terminal.
Use `argparse` instead of only `sys.argv` so your script looks closer to a real tool.

## Tasks

- Import `argparse`.
- Accept a CSV path as a positional argument.
- Accept an optional target column with a named flag such as `--target`.
- Add a default value for the target column.
- Call a `main()` function that receives parsed values.

## Why This Matters

Many coding tests and real projects become easier to reuse when you can run:

```bash
python main.py data/student_dev_ai_practice.csv --target test_score
```

That is much cleaner than editing values manually every time.

## Stretch Goal

- Add one more optional flag such as `--save-plots` or `--test-size`.
