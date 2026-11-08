def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    frequency = {}

    for char in str1:
        frequency[char] = frequency.get(char, 0) + 1

    for char in str2:
        if char not in frequency:
            return False

        frequency[char] -= 1

        if frequency[char] < 0:
            return False

    return all(count == 0 for count in frequency.values())


str1 = input("Enter a first text: ")
str2 = input("Enter a second text: ")
result = is_anagram(str1, str2)
print(result)