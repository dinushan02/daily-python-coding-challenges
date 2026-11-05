def first_non_repeating_character(text):
    if not text:
        return None

    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    for char in text:
        if frequency[char] == 1:
            return char

    return None


text = input("Enter your text: ")
result = first_non_repeating_character(text)
print(f"First non repeating character: {result}")