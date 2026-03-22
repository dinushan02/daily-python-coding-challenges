# Day 15: Break and Continue

# Stops the loop at 15 and skips numbers divisible by 3 before printing
for num in range(1, 21):
    if num == 15:
        break

    if num % 3 == 0:
        continue

    print(num)


print("\n" + "⭐" * 40)

print("""
🧠 Interview-Style Logical Question
❓ Write a Python program that:
➡️ Loops from 1 to 50
➡️ Skips numbers divisible by 5
➡️ Stops the loop when a number is divisible by both 3 and 7
""")

# Skips multiples of 5 and stops when a number is divisible by both 3 and 7
for number in range(1, 51):
    if (number % 3 == 0) and (number % 7 == 0):
        break

    if number % 5 == 0:
        continue

    print(number)









    