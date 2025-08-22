import random
import math

# trial.py


def greet_user(name):
    print(f"Hello, {name}! Welcome to the Python trial.")

def generate_random_numbers(count, lower=1, upper=100):
    numbers = []
    for _ in range(count):
        num = random.randint(lower, upper)
        numbers.append(num)
    return numbers

def calculate_statistics(numbers):
    total = sum(numbers)
    mean = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    stddev = math.sqrt(variance)
    return {
        'total': total,
        'mean': mean,
        'min': minimum,
        'max': maximum,
        'variance': variance,
        'stddev': stddev
    }

def print_statistics(stats):
    print("Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value:.2f}")

def main():
    print("=== Python Trial Program ===")
    name = input("Enter your name: ")
    greet_user(name)
    try:
        count = int(input("How many random numbers to generate? (10-20): "))
        if count < 10 or count > 20:
            print("Count must be between 10 and 20. Using default value 10.")
            count = 10
    except ValueError:
        print("Invalid input. Using default value 10.")
        count = 10

    numbers = generate_random_numbers(count)
    print(f"Generated numbers: {numbers}")

    stats = calculate_statistics(numbers)
    print_statistics(stats)

    print("Numbers sorted ascending:")
    print(sorted(numbers))

    print("Numbers sorted descending:")
    print(sorted(numbers, reverse=True))

    print("Thank you for using the trial program!")

if __name__ == "__main__":
    main()
    
