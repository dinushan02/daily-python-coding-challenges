"""
Day 26: Second Largest Unique Number

Problem Statement:
Given a list of integers, find the second largest unique number.

Requirements:
=> Take a list of integers from the user.
=> Remove duplicate numbers.
=> Find the second largest unique number.
=> If there are fewer than two unique numbers, display an appropriate message.
"""

def find_second_largest(numbers):

    unique_numbers = []

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    if len(unique_numbers) < 2:
        return None

    largest = unique_numbers[0]
    second_largest = unique_numbers[1]

    for number in unique_numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest:
            second_largest = number

    return second_largest


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = find_second_largest(numbers)

if result is None:
    print("No second largest number exists.")
else:
    print(f"Second largest: {result}")





    






    