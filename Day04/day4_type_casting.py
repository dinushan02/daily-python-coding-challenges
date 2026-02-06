# Day 4: Type Casting with Styled Output

# Getting inputs from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

# Calculations
age_in_months = age * 12

# Displaying outputs with a styled box
print("\n" + "="*40)
print("          USER INFORMATION          ")
print("="*40)
print(f"Name   : {name}")
print(f"Age    : {age} years ({age_in_months} months)")
print(f"Height : {height} centimeters")
print("="*40)
print("        Thank you for using        ")
print("="*40)





