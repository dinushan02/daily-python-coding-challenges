# Day 8: Tuples

my_tuple = ("Apple", "Banana", "Mango", "Apple", "Orange")
print(f"✅ Full Tuple: {my_tuple}")

# Accessing elements
print(f"✅ First item: {my_tuple[0]}")
print(f"✅ Last item: {my_tuple[-1]}")

# Tuple methods
print(f"✅ Index of Mango: {my_tuple.index("Mango")}")
print(f"✅ Count of Apple: {my_tuple.count("Apple")}")

# Converting tuple to list
tuple_to_list = list(my_tuple)
tuple_to_list.append("Pineapple")
print(f"✅ Converted List: {tuple_to_list}")


print("""
🧠 Interview-Style Logical Question
Given a tuple, return a new tuple containing only unique elements, keeping the original order.
""")
numbers = (1, 2, 2, 3, 1, 4)
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

result = tuple(unique_numbers)
print(f"Unique Tuple: {result}")












