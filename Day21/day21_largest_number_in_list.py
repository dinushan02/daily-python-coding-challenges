# Day 21: Largest Number in a List

numbers = [10, 9, 21, 30, 50, 40, 80]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(f"Largest number is {largest}")

# Using built-in function short one-line
# print(f"Largest number is {max(numbers)}")

print("\n" + "⭐" * 40)

print("""
🧠 Interview-Style Logical Question
❓ Given a list of numbers, find both the largest and second largest numbers without using built-in functions.
""")

numbers = [20, 9, 30, 40, 100, 70, 90]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(f"Largest number: {largest}")
print(f"Second largest number: {second_largest}")

# Even Simple Using built-in max()
"""numbers = [20, 9, 30, 40, 100, 70, 90]

largest = max(numbers)
numbers.remove(largest)
second_largest = max(numbers)

print(f"Largest number: {largest}")
print(f"Second largest number: {second_largest}")"""


