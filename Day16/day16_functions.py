# Day 16: Functions

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is Even"
    else:
        return f"{num} is Odd"

# Calling functions
result = add_numbers(10, 5)
print("Addition Result:", result)

print(check_even_odd(10))
print(check_even_odd(7))

print("\n" + "⭐" * 40)

print("""
🧠 Interview-Style Logical Question
❓ Write a function that takes a number as input and returns the factorial of that number.
""")

def factorial():
    try:
        num = float(input("Enter a number: "))

        if not num.is_integer():
            return "Please enter a whole number (no decimals like 3.5)"

        num = int(num)

        if num < 0:
            return "Factorial is not defined for negative numbers"

        result = 1
        for i in range(1, num + 1):
            result *= i

        return result

    except ValueError:
        return "Please enter only numbers"


print(factorial())



