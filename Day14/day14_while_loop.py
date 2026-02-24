# Day 14: While Loop

# Print all even numbers between 1 and 50
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1

# Count how many even numbers are between 1 and 50
i = 1
count = 0
while i <= 50:
    if i % 2 == 0:
        count += 1
    i += 1
print("Total even numbers:", count)

# Sum of all even numbers between 1 and 50
i = 1
total = 0
while i <= 50:
    if i % 2 == 0:
        total += i
    i += 1
print("Sum of all even numbers:", total)

print("\n⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")

print("""
🧠 Interview-Style Logical Question
❓ Write a Python program that asks the user for a number,
   then prints all numbers from that number down to 1 using a while loop.
""")

try:
    get_num_user = int(input("Enter the number: "))

    # Check for negative numbers
    if get_num_user < 0:
        print("❌ Negative numbers are not allowed. Please enter a positive number.")
    else:
        while get_num_user > 0:
            print(get_num_user)
            get_num_user -= 1

except ValueError:
    print("❌ You need to enter a valid integer number.")


