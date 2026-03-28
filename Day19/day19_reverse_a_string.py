# Day 19: Reverse a String

def reverse_string(text):
    return text[::-1]

while True:
    text = input("\nEnter a string: ").strip()

    if not text:
        print("Input cannot be empty!")
        continue

    # Allow only letters and spaces
    if all(char.isalpha() or char.isspace() for char in text):
        reversed_text = reverse_string(text)
        print(f"Reversed string: {reversed_text}")
    else:
        print("Please enter only letters (no numbers or symbols)!")

    user_continue = input("\nDo you want to continue (yes/no): ").strip().lower()
    if user_continue != "yes":
        print("Good bye👋")
        break

print("\n" + "⭐" * 40)

print("""
🧠 Interview-Style Logical Question
❓ Write a Python program that checks whether a given string is a palindrome (reads the same forward and backward).
➡️ Example:
➡️ Input: "madam" → Output: True
""")

def reverse_string(text):
    return text[::-1]

def check_palindrome(text):
    reversed_text = reverse_string(text)
    if reversed_text == text:
        return True
    else:
        return False

text = input("\nEnter a string: ")
result = check_palindrome(text)
print(f"Palindrome: {result}")










