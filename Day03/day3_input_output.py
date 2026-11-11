# Day 3: Input & Output
# Topic: Taking user input with input() and displaying results with print()
#
# What this program does:
#   1. Prints a formatted welcome banner
#   2. Asks the user for their name, age, and favorite language
#   3. Converts the age to an integer using int()
#   4. Displays a summary of the details using f-strings
#
# Key concepts:
#   - input()  -> always returns text (a string)
#   - int()    -> converts text to a whole number
#   - f-string -> inserts variable values directly into text
#   - \n       -> adds a new line

print("                          ===================================")
print("                                   USER INFORMATION          ")
print("                          ===================================")

print("\n                               Welcome to our system!")
print("           We are collecting these details for basic identification purposes.\n")

name = input("                          Enter your name: ")
age = int(input("                          Enter your age: "))
language = input("                          Enter your favorite language: ")

print("\n                          ===================================")
print("                                Your details have been")
print("                                recorded successfully!")
print("                          ===================================\n")

print("                          =============== RESULT ============")
print(f"                           ✅ Hello {name}!")
print(f"                           ✅ You are {age} years old.")
print(f"                           ✅ Your favorite language is {language}.")
print("                          ====================================")