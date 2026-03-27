# Day 18: Modules & Imports

import math
import random

# Using math module
num = 25
sqrt_result = math.sqrt(num)

# Using random module
random_num = random.randint(1, 10)

# Print results with proper formatting
print(f"Square root of 25: {sqrt_result:.2f}")
print(f"Random number between 1 and 10: {random_num}")

print("\n" + "⭐" * 40)

print("""
🧠 Interview-Style Logical Question
❓ Write a Python program that:
➡️ Imports the random module
️➡️ Generates 5 random numbers between 1 and 50
➡️ Returns the maximum number among them
""")

import random  # Import random module

max_number = 0  # Store the maximum value

# Generate 5 random numbers
for i in range(5):
    num = random.randint(1, 50)
    print(f"Generated Number: {num}")

    if num > max_number:
        max_number = num  # Update maximum

print(f"Maximum Number: {max_number}")












