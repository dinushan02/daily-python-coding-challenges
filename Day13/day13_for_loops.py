# Day 13: For Loop Basics

print("Numbers 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")

print("\n\nCharacters in a string:")
word = "Kindness is God"
for ch in word:
    print(ch, end=" ")

print("\n\nLooping through a list:")
programming_languages = ["Python", "Java", "C", "C#"]
for pro_lang in programming_languages:
    print(pro_lang)

print("\nSum of numbers from 1 to 10:")
total = 0
for num in range(1, 11):
    total += num
print(f"Sum: {total}")

print("\n⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")

print("""
🧠 Interview-Style Logical Question 
❓ Write a Python program that prints all even numbers between 1 and 50, and also counts how many even numbers were found.
""")

count = 0

for num in range(1, 51):
    if num % 2 == 0:
        print(num, end=" ")
        count += 1

print(f"\nTotal even numbers: {count}")