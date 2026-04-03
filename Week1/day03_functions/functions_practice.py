def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def average(numbers: list[float]) -> float:
    """Return the average of a list of numbers."""
    if not numbers:
        raise ValueError("numbers cannot be empty")
    return sum(numbers) / len(numbers)


def is_passing(score: float, passing_grade: float = 5.5) -> bool:
    """Return whether a score is passing."""
    return score >= passing_grade


def print_mini_report(a: float, b: float, numbers: list[float], score: float) -> None:
    """Print a short report using the helper functions."""
    print("Mini report")
    print(f"add({a}, {b}) = {add(a, b)}")
    print(f"average({numbers}) = {average(numbers):.2f}")
    print(f"is_passing({score}) = {is_passing(score)}")
    print()


def main() -> None:
    """Run example calls for each function."""
    print(add(2, 3))
    print(add(10.5, 4.5))

    print(average([1, 2, 3, 4]))
    print(average([5.5, 6.0, 7.5]))

    print(is_passing(4.8))
    print(is_passing(7.2))

    print()
    print_mini_report(4, 6, [1, 5, 8, 3, 4, 10], 6.3)
    print_mini_report(1.5, 2.5, [7.0, 8.5, 9.0], 5.0)


if __name__ == "__main__":
    main()
