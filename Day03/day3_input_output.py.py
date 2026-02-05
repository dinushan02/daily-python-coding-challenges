# Day 3: Input & Output

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