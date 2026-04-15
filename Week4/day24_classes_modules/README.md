# Day 24 - Classes, Modules, and Imports

Turn a single long script into a small project with multiple files.

Before starting, read [CLASS_BASICS.md](CLASS_BASICS.md) if `__init__`, `self`, `@property`, or underscore naming still feels shaky.

## Tasks

- Create one class such as `TrainingConfig` or `StudentRecord`.
- Move your CSV helpers into `data_utils.py`.
- Move your model code into `model_utils.py`.
- Keep `main.py` focused on orchestration instead of low-level details.
- Write 3 sentences explaining why this is easier to maintain.
- Prefer `@dataclass` for simple data containers.
- Add type hints to class attributes and public functions.
- Give your class one useful method such as `from_args(...)` or `summary()`.

## Quick Class Notes

- `__init__(self, ...)` is the setup method that runs when you create an object.
- `self` means "this object" and is how you store or read that object's data.
- A normal method usually has a plain name like `summary()` or `scale()`.
- Only use double underscores for special Python methods such as `__init__` or `__repr__`.
- `@property` lets a method behave like an attribute, which is useful for computed values.
- `@dataclass` is often the cleanest choice when your class mostly stores data.

## Mini Example

```python
from dataclasses import dataclass


@dataclass
class StudentRecord:
    name: str
    python_score: float
    math_score: float

    @property
    def average_score(self) -> float:
        return (self.python_score + self.math_score) / 2

    def summary(self) -> str:
        return f"{self.name}: average={self.average_score:.1f}"
```

This example shows 3 different class ideas:

- stored data: `name`, `python_score`, `math_score`
- computed value: `average_score`
- normal behavior method: `summary()`

## Why This Matters

A class is useful when several values belong together.
Modules are useful when one file starts doing too many jobs.
This is one of the biggest steps from beginner scripts to cleaner software.
