"""
Day 27: Remove Duplicates from a List

Problem Statement:
Given a list of integers, create a new list containing only
the unique elements while preserving their original order.

Requirements:
=> Take a list of integers from the user.
=> Remove duplicate numbers.
=> Preserve the original order of the numbers.
=> Display the list containing only unique numbers.
"""


def remove_duplicates(numbers):
    unique_numbers = []
    seen = set()

    for num in numbers:
        if num not in seen:
            unique_numbers.append(num)
            seen.add(num)

    return unique_numbers


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    result = remove_duplicates(numbers)
    print(f"Unique numbers: {result}")