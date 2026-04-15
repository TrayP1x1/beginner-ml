# Class Basics Refresher

This note exists for the moment when classes feel half-familiar but still slippery.
Use it as a quick reset before or during Day 24.

## What A Class Is

A class is a blueprint.
An object is one actual thing created from that blueprint.

Example:

```python
class Student:
    pass


student_a = Student()
student_b = Student()
```

`Student` is the class.
`student_a` and `student_b` are objects created from that class.

## What `__init__` Does

`__init__` runs when you create an object.
Its job is usually to store values on `self`.

```python
class Vector:
    def __init__(self, values: list[float]):
        self.values = values
```

Usage:

```python
v = Vector([1.0, 2.0, 3.0])
print(v.values)
```

Read it like this:

- `self` means "this object"
- `values: list[float]` is a type hint
- `self.values = values` stores the incoming value on the object

## Why `values: list[int]` Or `list[float]` Is Optional

These are both valid:

```python
def __init__(self, values):
```

```python
def __init__(self, values: list[int]):
```

The second version is usually nicer because it tells you and your editor what type is expected.
Python does not require the type hint to run the code.

Use type hints when you can.
They make code easier to understand and debug.

## What `self` Means

`self` is the current object.
It is how one method accesses the data stored on that object.

```python
class Student:
    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        return f"Hi, I am {self.name}"
```

Without `self`, the object would not know which `name` belongs to which student.

## Normal Methods vs Special Methods

Most methods are normal methods:

```python
class Dog:
    def bark(self) -> str:
        return "woof"
```

Some methods have double underscores on both sides, such as:

- `__init__`
- `__repr__`
- `__len__`

These are special Python methods, often called dunder methods.
You do not add `__` to every method name.

Use:

```python
def average_score(self) -> float:
```

not:

```python
def __average_score__(self) -> float:
```

unless you are intentionally implementing one of Python's special methods.

## What `@property` Means

`@property` lets a method behave like an attribute.
That is useful when a value is computed from other values.

```python
class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def area(self) -> float:
        return 3.14159 * self.radius ** 2
```

Usage:

```python
c = Circle(2.0)
print(c.area)
```

Notice this:

- `c.area` is correct
- `c.area()` is wrong because `area` is being used like data, not like a normal method

`@property` is helpful when the result should feel like a value that belongs to the object.

## What `@dataclass` Changes

For simple data containers, `@dataclass` saves you from writing a basic `__init__` by hand.

```python
from dataclasses import dataclass


@dataclass
class ScoreRow:
    name: str
    math_score: float
    python_score: float
```

This automatically gives you an `__init__` similar to:

```python
def __init__(self, name: str, math_score: float, python_score: float):
    self.name = name
    self.math_score = math_score
    self.python_score = python_score
```

You can still add your own methods:

```python
from dataclasses import dataclass


@dataclass
class ScoreRow:
    name: str
    math_score: float
    python_score: float

    @property
    def average_score(self) -> float:
        return (self.math_score + self.python_score) / 2
```

## Underscore Naming Cheatsheet

These names do not all mean the same thing:

- `_name`: usually means "internal use" by convention
- `__name__`: usually a special Python method or special built-in name
- `_`: often means "I do not care about this variable"

Examples:

```python
def _helper() -> None:
    print("internal helper")
```

```python
for _ in range(3):
    print("hello")
```

```python
if __name__ == "__main__":
    main()
```

Important:

- `_helper` is just a naming convention, not a true private method
- `__init__` is a special method name recognized by Python
- `__name__` is a built-in variable that tells Python how the file is being run

## Are These Keywords

Not all of them.

Python keywords are words like:

- `class`
- `def`
- `return`
- `if`
- `for`
- `try`
- `except`

But these are not keywords in the same sense:

- `self`
- `__init__`
- `@property`

`self` is just the normal name used for the current object.
`__init__` is a special method name.
`@property` is a decorator.

## Tiny Example To Study

```python
from dataclasses import dataclass


@dataclass
class Vector:
    values: list[float]

    @property
    def size(self) -> int:
        return len(self.values)

    def scale(self, factor: float) -> list[float]:
        return [value * factor for value in self.values]
```

Read this class like this:

- `values` is stored data
- `size` is computed data exposed as a property
- `scale(...)` is a normal method because it performs an action

## Rules To Remember

- Use `__init__` when you want to set up an object manually.
- Use `@dataclass` when your class is mostly storing data.
- Use `@property` when a computed value should feel like an attribute.
- Use normal method names like `summary()` or `scale()`.
- Do not put `__` around every method name.
- Add type hints when possible because they make class code easier to read.
