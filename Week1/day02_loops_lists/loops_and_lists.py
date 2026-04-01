def get_even_numbers(numbers: list[int]) -> list[int]:
    return [number for number in numbers if number % 2 == 0]


def calculate_total(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        total += number
    return total


def calculate_average(numbers: list[int]) -> float:
    if not numbers:
        raise ValueError("numbers must not be empty")
    return calculate_total(numbers) / len(numbers)


def main() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    print("Indexed values:")
    for index, number in enumerate(numbers):
        print(f"{index}: {number}")

    even_numbers = get_even_numbers(numbers)
    total = calculate_total(numbers)
    average = calculate_average(numbers)

    print()
    print("Even numbers:", even_numbers)
    print("Total:", total)
    print("Average:", average)


if __name__ == "__main__":
    main()
