# Day 11: If-Else Statements

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote! ✅")
else:
    print("Sorry, you are not eligible to vote yet. ❌")

print("\n⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")

print("""
🧠 Interview-Style Logical Question
❓ Write a Python program that asks the user to enter a number, validates the input, and then prints whether the number is positive, negative, or zero.
""")

def check_number():
    try:
        number = float(input("Enter a number: "))

        if number > 0:
            print(f"{number} is positive.")
        elif number < 0:
            print(f"{number} is negative.")
        else:
            print(f"{number} is zero.")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")

check_number()

"""
✅ In this program, I used a function called check_number() to organize the logic clearly.

✅ Inside the function, I wrapped the input conversion inside a try-except block to validate 
the user input, because converting a string to a float can raise a ValueError if the user enters something that is not numeric.

✅ Once I successfully convert the input to a number, I check whether it is positive, negative, or zero using simple if-elif-else conditions.

✅ This structure makes the program more readable, prevents runtime errors, and ensures the input is properly validated before running the main logic.
"""












