# Topic: Set Operations + Unique Elements Preserving Order
# Date: 2026-02-14
# Description: Demonstrates basic set operations and an interview-style logic problem.

print("Example basic set operations")
print("----------------------------")

list1 = [1, 2, 2, 3, 4]
list2 = [3, 4, 4, 5, 6]

# Convert lists to sets to remove duplicates and enable set operations
set1 = set(list1)
set2 = set(list2)

print(f"✅ Unique elements in list1: {set1}")

# Union: combines all unique elements from both sets
print("✅ Union: ", set1 | set2)

# Intersection: finds elements common to both sets
print("✅ Intersection: ", set1 & set2)

# Difference: finds elements in set1 that are not in set2
print("✅ Difference (set1 - set2): ", set1 - set2)

# Membership check: verifies if an element exists in the set
print("✅ Is 2 in set1?", 2 in set1)


print("\nInterview-style logical question: unique elements preserving order")
print("------------------------------------------------------------------")

numbers = [4, 5, 2, 4, 3, 5, 1]
seen = set()
duplicates = set()
unique_ordered = []

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

for num in numbers:
    if num not in duplicates:
        unique_ordered.append(num)

print(f"Unique numbers preserving order: {unique_ordered}")


"""
✅✅✅ To understand the above interview logic question:

numbers = [4, 5, 2, 4, 3, 5, 1]

# used to track numbers that have appeared at least once (fast lookup + no duplicates)
seen = set()

# used to store numbers that appear more than once (each stored only once)
duplicates = set()

# used to store the final unique numbers in original order
unique_ordered = []

# first loop: find all numbers that are duplicates
for num in numbers:
    if num in seen:
        duplicates.add(num)      # if already seen, it's a duplicate
    else:
        seen.add(num)            # first time seeing the number

# second loop: collect only numbers that are not duplicates
for num in numbers:
    if num not in duplicates:
        unique_ordered.append(num)

print(f"Unique numbers preserving order: {unique_ordered}")
"""


