# Day 10: Dictionaries

person = {"name": "Arutperunjothi", "age": 24, "city": "Kilinochchi"}
print(f"✅ Original dictionary: {person}")

# Add a new key-value pair
person["country"] = "Sri Lanka"
print(f"✅ After adding country: {person}")

# Update an existing value
person["age"] = 25
print(f"✅ After updating age: {person}")

# Delete a key-value pair
del person["city"]
print(f"✅ After deleting city: {person}")

# Print keys and values
print(f"\n➡️ Keys: {person.keys()}")
print(f"➡️ Values: {person.values()}")

print("\n⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")

print("""
🧠 Interview-Style Logical Question:
❓ Given a list of tuples representing student names and scores, create a dictionary and return the student with the highest score.
""")

students_scores = [("Ram", 70), ("Sam", 90), ("Kumar", 85)]

student_dict = dict(students_scores)

highest_student = max(student_dict, key=student_dict.get)

result = {highest_student: student_dict[highest_student]}
print(result)

"""
✅✅✅ To understand the above interview logic question: 👇

# Input list of tuples
students_scores = [('Alice', 85), ('Bob', 92), ('Charlie', 88)]

# Convert list of tuples to dictionary
student_dict = dict(students_scores)

# Find the student with the highest score
highest_student = max(student_dict, key=student_dict.get)

# Output the result as a dictionary
result = {highest_student: student_dict[highest_student]}
print(result)

Explanation:
🔷 dict(students_scores) converts the list of tuples into a dictionary: {'Alice': 85, 'Bob': 92, 'Charlie': 88}
🔷 max(student_dict, key=student_dict.get) finds the key with the maximum value (highest score).
🔷 We create a dictionary {highest_student: student_dict[highest_student]} to match the expected output format.
"""