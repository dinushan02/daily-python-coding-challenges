# Day 12: Nested Conditions

age = int(input("Enter your age: "))

if age >= 18:
    has_id = input("Do you have your voter ID? (yes/no): ").lower()

    if has_id == "yes":
        print("You are eligible to vote! 🗳️")
    else:
        print("You must bring your voter ID to vote.")
else:
    print("Sorry, you are not old enough to vote yet.")


print("\n⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")


print("""
🧠 Interview-Style Logical Question
❓ Write a program that checks if a number is even or odd, and if it is even, also check whether it is divisible by 4.
""")

number = int(input("Enter a number: "))

if number % 2 == 0:
    if number % 4 == 0:
        print("Even and divisible by 4")
    else:
        print("Even but not divisible by 4")
else:
    print("Odd")



