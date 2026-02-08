# Day 6: Strings and String Methods with Boxed Output

# Get input from the user and remove extra spaces
text = input("Enter text: ").strip()

# String calculations and transformations
total_chars = len(text)
uppercase_text = text.upper()
lowercase_text = text.lower()
reversed_text = text[::-1]
word_count = len(text.split())
is_palindrome = text.lower() == reversed_text.lower()

title_case_text = text.title()
starts_with_m = text.lower().startswith("m")
ends_with_m = text.lower().endswith("m")
replaced_text = text.replace("a", "#")

# Display results in a styled box
print("\n" + "="*50)
print("                   TEXT ANALYSIS")
print("="*50)
print(f"Original Text      : {text}")
print(f"Total Characters   : {total_chars}")
print(f"Uppercase          : {uppercase_text}")
print(f"Lowercase          : {lowercase_text}")
print(f"Reversed           : {reversed_text}")
print(f"Word Count         : {word_count}")
print(f"Is Palindrome      : {is_palindrome}")
print(f"Title Case         : {title_case_text}")
print(f"Starts with 'm'    : {starts_with_m}")
print(f"Ends with 'm'      : {ends_with_m}")
print(f"Replaced (a ➡️ #) : {replaced_text}")
print("="*50)



