# Day 22: Find Frequency of Elements

numbers = [1, 2, 2, 3, 4, 1, 2, 4, 3, 2]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Element Frequency:")
for key, value in frequency.items():
    print(f"{key} appears {value} times")

"""
Simple Explanation
==================
⭐ Loop through each number
⭐ If it's already in dictionary → increase count
⭐ If not → add it with count = 1
"""

# We can also do this using Python’s built-in tool:
"""from collections import Counter

numbers = [1, 2, 2, 3, 4, 1, 2, 4, 3, 2]

frequency = Counter(numbers)

print(frequency)"""

print("\n" + "⭐" * 40)

print("""
🧠 𝗜𝗻𝘁𝗲𝗿𝘃𝗶𝗲𝘄-𝗦𝘁𝘆𝗹𝗲 𝗟𝗼𝗴𝗶𝗰𝗮𝗹 𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻
❓ Given a list, find the element that appears the most (highest frequency) without using built-in functions.
""")

numbers = [1, 2, 2, 3, 4, 1, 2, 4, 3, 2]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

max_count = 0
max_element = None

for key, value in frequency.items():
    if value > max_count:
        max_count = value
        max_element = key

print(f"{max_element} appears the most ({max_count} times)")


