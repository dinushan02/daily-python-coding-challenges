# Day 17: Return Values

# Function to calculate square
def square(num):
    return num * num

# Function to check number type
def check_number(num):
    if num > 0:
        return f"{num} is Positive"
    elif num < 0:
        return f"{num} is Negative"
    else:
        return f"{num} is Zero"

# Using returned values
result = square(5)
print("Square of 5:", result)

print(check_number(-3))
print(check_number(10))

print("\n" + "⭐" * 40)

print("""
🧠 Interview-Style Logical Question
❓ Write a function that takes a number and returns True if it is a prime number, otherwise returns False.
""")

# Function to check prime number
def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

# User input and output
try:
    num = int(input("Enter the number: "))
    print(is_prime(num))
except ValueError:
    print("Please enter only integer number")

# 💡 Explanation:
#
# In the "is_prime(number)" function:
# - We use "for i in range(2, number):" because:
#     1. 1 is a factor of every number, so no need to check it.
#     2. The number itself is also a factor, so no need to check it.
#     3. We only need to check numbers between 2 and (number-1).
# - If the number is divisible by any value in this range, it is NOT prime.
# - If no divisors are found in this range, the number is PRIME.















