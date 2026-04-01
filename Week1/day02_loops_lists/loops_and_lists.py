def list_of_numbers() -> list[int]:
    numbers = []

    while True: 
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input.lower() == 'done' or len(numbers) >= 8:
            break
        else:
            try:
                numbers.append(int(user_input))
            except ValueError:
                print("Invalid input. Please enter a number or 'done' to finish.")
    print()
    return numbers

def get_even_numbers(numbers: list[int]) -> list[int]: 
    even_numbers = [number for number in numbers if number % 2 == 0]
    return even_numbers

def calculate_average(numbers: list[int]) -> float:
    
    if len(numbers) == 0:
        return 0.0
    
    total = 0
    for number in numbers:
        total += number

    print(f"Total: {total}")
    return total / len(numbers)


def main(numbers: list[int]) -> None:
    print(f"Even numbers are: {get_even_numbers(numbers)}")
    print(f"Average of {numbers} is {calculate_average(numbers)}", end="\n\n")
    for index, value in enumerate(numbers):
        print(f"Index and value pairs are {index, value}")


if __name__ == "__main__":
    lst = list_of_numbers()
    print(f"You entered: {lst}")
    main(lst)

7