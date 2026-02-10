# Day 7: Lists

# All List Methods in Python (With Simple Examples)
# Below are the most important list methods you must know as a Python developer.

# 1️⃣ append() — Add item at the end
fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(fruits)   # ['Apple', 'Banana', 'Mango']


# 2️⃣ insert() — Add item at a specific position
fruits = ["Apple", "Mango"]
fruits.insert(1, "Banana")
print(fruits)   # ['Apple', 'Banana', 'Mango']


# 3️⃣ extend() — Add multiple items
fruits = ["Apple", "Banana"]
fruits.extend(["Mango", "Orange"])
print(fruits)   # ['Apple', 'Banana', 'Mango', 'Orange']


# 4️⃣ remove() — Remove a specific item
fruits = ["Apple", "Banana", "Mango"]
fruits.remove("Banana")
print(fruits)   # ['Apple', 'Mango']


# 5️⃣ pop() — Remove item by index
# If no index → removes the last item.
fruits = ["Apple", "Banana", "Mango"]
fruits.pop(1)
print(fruits)   # ['Apple', 'Mango']


# 6️⃣ clear() — Remove all items
fruits = ["Apple", "Banana", "Mango"]
fruits.clear()
print(fruits)   # []


# 7️⃣ index() — Find position of an item
fruits = ["Apple", "Banana", "Mango"]
print(fruits.index("Banana"))   # 1


# 8️⃣ count() — Count how many times an item appears
numbers = [1, 2, 2, 3, 2]
print(numbers.count(2))   # 3


# 9️⃣ sort() — Sort ascending
numbers = [5, 2, 8, 1]
numbers.sort()
print(numbers)   # [1, 2, 5, 8]


# 🔟 sort(reverse=True) — Sort descending
numbers = [5, 2, 8, 1]
numbers.sort(reverse=True)
print(numbers)   # [8, 5, 2, 1]


# 1️⃣1️⃣ reverse() — Reverse list order
letters = ["a", "b", "c"]
letters.reverse()
print(letters)   # ['c', 'b', 'a']


# 1️⃣2️⃣ copy() — Make a separate copy
fruits = ["Apple", "Banana"]
new_list = fruits.copy()
print(new_list)   # ['Apple', 'Banana']

print("\n🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷")
print("""
🎯 Simple Task (Beginner Level)
✅ Task:
Create a list of 5 movies
➡️ Add 1 more
➡️ Remove 1
➡️ Print first, last, and total movies
""")

movies = ["RRR", "Avatar", "KGF", "Inception", "Leo"]
print("My movies:", movies)

movies.append("Interstellar")
print("After adding:", movies)

movies.remove("KGF")
print("After removing:", movies)

print("First movie:", movies[0])
print("Last movie:", movies[-1])
print("Total movies:", len(movies))


print("\n🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷🔷")
print("""
💼 Interview-Level List Challenge (Advanced)
❓ Problem:
⭐ Given a list of numbers,
⭐ remove duplicates,
⭐ sort the list,
⭐ and print only even numbers.
""")

numbers = [4, 7, 2, 4, 9, 2, 8, 6, 8]
print("Original List:", numbers)

unique_numbers = list(set(numbers))
unique_numbers.sort()
print("Unique Sorted List:", unique_numbers)

even_numbers = [n for n in unique_numbers if n % 2 == 0]
print("Even Numbers Only:", even_numbers)




