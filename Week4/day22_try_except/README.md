# Day 22 - Error Handling With `try` and `except`

Write `safe_csv_reader.py` and practice handling common mistakes without crashing confusingly.

## Tasks

- Try to open a CSV file path from a variable.
- Catch `FileNotFoundError` and print a helpful message.
- Catch `ValueError` when converting a string to a number.
- Add a small `finally` message such as `finished attempt`.
- Explain in comments when you should catch an error and when you should let it fail.
- Raise your own `ValueError` or `KeyError` with a clearer message when required columns are missing.
- Separate parsing errors from file-path errors.
- Return clean values from helper functions instead of only printing inside `except` blocks.

## Why This Matters

In a coding test, simple error handling makes your code look more professional.
It also helps you debug faster when a path, column, or conversion is wrong.

## Stretch Goal

- Create a function `load_scores(path)` that raises a clear error if the file is empty.
