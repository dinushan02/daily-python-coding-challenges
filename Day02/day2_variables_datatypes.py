# Day 2: Variables & Data Types
# Topic: The four basic data types in Python

# str (String): text, always written inside quotes
name = "Dinushan"

# int (Integer): whole numbers, no decimal point
age = 24

# bool (Boolean): only True or False (note the capital letters)
is_student = True

# float (Float): numbers with a decimal point
height = 1.75

# Display each variable using f-strings
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Is Student: {is_student}")
print(f"Height: {height}")

# Check the data type of each variable using type()
print(f"Type of name: {type(name)}")              # <class 'str'>
print(f"Type of age: {type(age)}")                # <class 'int'>
print(f"Type of is_student: {type(is_student)}")  # <class 'bool'>
print(f"Type of height: {type(height)}")          # <class 'float'>