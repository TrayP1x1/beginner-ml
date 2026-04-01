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
  tests/
```

## Why This Matters

This is the structure that helps you most in a timed test.
It is simple, readable, and easy to explain aloud.
