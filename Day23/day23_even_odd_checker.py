# Day 23: Even/Odd Checker

def check_even_odd_number(num):
    return "even" if num % 2 == 0 else "odd"


def main():
    try:
        num = int(input("Enter a number: "))
        result = check_even_odd_number(num)
        print(f"{num} is {result}")
    except ValueError:
        print("Please only enter a whole number!")


if __name__ == "__main__":
    main()


print("\n" + "⭐" * 40)

print("""
🧠 Interview-Style Logical Question
❓ Write a Python program that prints all even numbers between 1 and 100 and counts how many even numbers exist.
""")

count = 0

for num in range(1, 101):
    if num % 2 == 0:
        print(num, end=" ")
        count += 1

print(f"\n\nTotal even numbers between 1 and 100 are {count}")





