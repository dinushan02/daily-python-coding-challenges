# Day 20: Count Vowels in a Sentence

def count_vowels(user_sentence):
    vowels = "aeiou"

    count = 0
    for char in user_sentence.lower():
        if char.isalpha() and char in vowels:
            count += 1

    return count


user_sentence = input("Enter your sentence: ")
result = count_vowels(user_sentence)
print(f"Total number of vowels is {result}")


print("\n" + "⭐" * 40)


print("""
🧠 Interview-Style Logical Question
❓ Write a Python program that counts both vowels and consonants in a given sentence.
➡️ Example:
➡️ Input: "Python" → Output: Vowels: 1, Consonants: 5
""")

def count_vowels_consonants(user_sentence):
    vowels = "aeiou"

    vowel_count = 0
    consonant_count = 0

    for char in user_sentence.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


user_sentence = input("Enter your sentence: ")
vowels, consonants = count_vowels_consonants(user_sentence)

print(f"Total number of vowels is {vowels}")
print(f"Total number of consonants is {consonants}")