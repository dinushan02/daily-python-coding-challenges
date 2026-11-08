# Day 30 – Valid Anagram

**Difficulty:** Beginner to Intermediate

**Topics:** Python Strings, Dictionaries, Frequency Counting

## Problem Description

Given two strings, determine whether they are anagrams of each other.

Two strings are anagrams if they contain exactly the same characters with the same frequencies, but their character order can be different.

Return `True` if the two strings are anagrams. Otherwise, return `False`.

## Examples

### Example 1

**Input:**
```python
str1 = "listen"
str2 = "silent"
```

**Output:**
```python
True
```

**Explanation:**

Both strings contain exactly the same characters with the same frequencies.

### Example 2

**Input:**
```python
str1 = "hello"
str2 = "world"
```

**Output:**
```python
False
```

**Explanation:**

The two strings contain different characters.

### Example 3

**Input:**
```python
str1 = "aabb"
str2 = "bbaa"
```

**Output:**
```python
True
```

**Explanation:**

Both strings contain two `a` characters and two `b` characters.

---

## Approach 1 – Using Two Dictionaries

### Python Solution

```python
def is_anagram(str1, str2):

    # Check whether both strings have the same length.
    if len(str1) != len(str2):
        return False

    # Create two dictionaries to store character frequencies.
    str1_frequency = {}
    str2_frequency = {}

    # Count the frequency of each character in the first string.
    for str1_char in str1:
        str1_frequency[str1_char] = str1_frequency.get(str1_char, 0) + 1

    # Count the frequency of each character in the second string.
    for str2_char in str2:
        str2_frequency[str2_char] = str2_frequency.get(str2_char, 0) + 1

    # Compare both frequency dictionaries.
    return str1_frequency == str2_frequency


# Get the first string from the user.
str1 = input("Enter a first text: ")

# Get the second string from the user.
str2 = input("Enter a second text: ")

# Call the function and store the result.
result = is_anagram(str1, str2)

# Display the result.
print(result)
```

## Line-by-Line Explanation

### 1. Function Definition

```python
def is_anagram(str1, str2):
```

- Defines a function named `is_anagram`.
- Accepts two strings as parameters.

### 2. String Length Validation

```python
if len(str1) != len(str2):
    return False
```

- `len()` returns the number of characters in a string.
- Anagrams must have equal lengths.
- If the lengths are different, the function immediately returns `False`.

### 3. Dictionary Initialization

```python
str1_frequency = {}
str2_frequency = {}
```

- Creates two empty dictionaries.
- Each dictionary stores characters as keys and their frequencies as values.

### 4. First Frequency Loop

```python
for str1_char in str1:
    str1_frequency[str1_char] = str1_frequency.get(str1_char, 0) + 1
```

- Iterates through every character in the first string.
- `.get()` retrieves the existing frequency.
- If the character doesn't exist, it returns `0`.
- Adds `1` to the frequency.

### 5. Second Frequency Loop

```python
for str2_char in str2:
    str2_frequency[str2_char] = str2_frequency.get(str2_char, 0) + 1
```

- Iterates through the second string.
- Counts the frequency of each character.
- Stores the results in the second dictionary.

### 6. Dictionary Comparison

```python
return str1_frequency == str2_frequency
```

- Compares both dictionaries.
- Checks whether their keys and corresponding values are identical.
- Returns `True` if they match and `False` otherwise.
- Dictionary insertion order does not affect equality.

### 7. User Input

```python
str1 = input("Enter a first text: ")
str2 = input("Enter a second text: ")
```

- Accepts two strings from the user.

### 8. Function Call

```python
result = is_anagram(str1, str2)
```

- Calls the function with both input strings.
- Stores the returned Boolean value in `result`.

### 9. Display Result

```python
print(result)
```

- Displays `True` or `False`.

---

## Approach 2 – Using One Dictionary

This approach uses only one dictionary to count and compare character frequencies.

### Python Solution

```python
def is_anagram(str1, str2):

    # Check whether both strings have the same length.
    if len(str1) != len(str2):
        return False

    # Create one dictionary to store character frequencies.
    frequency = {}

    # Count characters in the first string.
    for char in str1:
        frequency[char] = frequency.get(char, 0) + 1

    # Decrease frequencies using characters from the second string.
    for char in str2:

        # Check whether the character exists in the dictionary.
        if char not in frequency:
            return False

        # Decrease the character frequency by one.
        frequency[char] -= 1

        # Check whether any frequency becomes negative.
        if frequency[char] < 0:
            return False

    # Check whether all character frequencies are zero.
    return all(count == 0 for count in frequency.values())


# Get the first string from the user.
str1 = input("Enter a first text: ")

# Get the second string from the user.
str2 = input("Enter a second text: ")

# Call the function and store the result.
result = is_anagram(str1, str2)

# Display the result.
print(result)
```

## Important Concepts Explained

### 1. Dictionary Frequency Counting

```python
frequency[char] = frequency.get(char, 0) + 1
```

Increases the frequency of each character in the first string.

### 2. Dictionary Membership Checking

```python
if char not in frequency:
    return False
```

Checks whether the character from the second string exists in the dictionary.

### 3. Decreasing Frequencies

```python
frequency[char] -= 1
```

Decreases the frequency when a matching character is found in the second string.

### 4. Negative Frequency Validation

```python
if frequency[char] < 0:
    return False
```

Detects when a character occurs more frequently in the second string than in the first.

### 5. Using the all() Function

```python
return all(count == 0 for count in frequency.values())
```

- `.values()` retrieves all dictionary values.
- `all()` checks whether every value satisfies the condition.
- Returns `True` only when all frequencies are zero.

---

## Expected Interaction

**Example 1:**

```text
Enter a first text: listen
Enter a second text: silent
True
```

**Example 2:**

```text
Enter a first text: hello
Enter a second text: world
False
```

**Example 3:**

```text
Enter a first text: aabb
Enter a second text: bbaa
True
```

---

## Test Cases

| # | First String | Second String | Expected Output |
|---|---|---|---|
| 1 | `"listen"` | `"silent"` | `True` |
| 2 | `"hello"` | `"world"` | `False` |
| 3 | `"aabb"` | `"bbaa"` | `True` |
| 4 | `"rat"` | `"car"` | `False` |
| 5 | `"a"` | `"a"` | `True` |
| 6 | `""` | `""` | `True` |

**Testing Result: 6/6 Test Cases Passed**

---

## Time and Space Complexity

Both approaches have the same asymptotic complexity.

### Time Complexity: O(n)

- First loop processes the first string: O(n).
- Second loop processes the second string: O(n).
- Dictionary comparison or final frequency validation takes O(k).

Overall: O(n).

### Space Complexity: O(k)

- `k` represents the number of distinct characters.
- The dictionaries store character frequencies.
- Two dictionaries still use O(k) auxiliary space.

---

## Key Concepts Learned

- Python Strings
- Dictionary Data Structures
- Dictionary Frequency Counting
- Dictionary `.get()` Method
- Dictionary Membership Checking
- Dictionary Equality Comparison
- `all()` Built-in Function
- Two-Dictionary Approach
- One-Dictionary Approach
- Time and Space Complexity

## What I Learned

In this challenge, I learned how to determine whether two strings are anagrams using Python dictionaries.

Initially, I worked with two dictionaries to count and compare character frequencies.

After understanding that approach, I challenged myself to solve the same problem using only one dictionary by increasing and decreasing character frequencies.

I also learned how to use the `all()` function to verify whether every frequency has returned to zero.

This challenge helped me understand how different approaches can solve the same problem and how dictionaries make frequency-counting problems efficient.

---

**Day 30 Completed!** 🚀

*100 Days, 100 Coding Challenges – Keep Learning, Keep Building!*