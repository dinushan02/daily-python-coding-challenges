# Day 29 – First Non-Repeating Character

**Difficulty:** Beginner to Intermediate

**Topic:** Strings and Dictionaries

## Problem Description

Given a string, find the first character that appears only once.

If every character appears more than once, return `None`.

### Examples

**Example 1**

Input:
```python
"aabbcde"
```

Output:
```python
"c"
```

Explanation:
- `a` appears 2 times.
- `b` appears 2 times.
- `c` appears 1 time.
- `d` appears 1 time.
- `e` appears 1 time.

The first non-repeating character is `c`.

**Example 2**

Input:
```python
"swiss"
```

Output:
```python
"w"
```

**Example 3**

Input:
```python
"aabbcc"
```

Output:
```python
None
```

## Python Solution

```python
def first_non_repeating_character(text):
    # Check whether the input string is empty.
    if not text:
        return None

    # Create an empty dictionary to store character frequencies.
    frequency = {}

    # First loop: Count how many times each character appears.
    for char in text:

        # Get the current count and increase it by 1.
        frequency[char] = frequency.get(char, 0) + 1

    # Second loop: Check characters in their original order.
    for char in text:

        # Check whether the current character appears only once.
        if frequency[char] == 1:
            return char

    # Return None if every character appears more than once.
    return None


# Get input from the user.
text = input("Enter your text: ")

# Call the function and store its result.
result = first_non_repeating_character(text)

# Display the result.
print(f"First non-repeating character: {result}")
```

## Line-by-Line Explanation

### 1. Function Definition

```python
def first_non_repeating_character(text):
```

- `def` defines a function.
- `first_non_repeating_character` is the function name.
- `text` is the input parameter that receives a string.

### 2. Empty String Validation

```python
if not text:
    return None
```

- Checks whether the input string is empty.
- If the string is empty, the function immediately returns `None`.
- This prevents unnecessary processing.

### 3. Dictionary Initialization

```python
frequency = {}
```

- Creates an empty dictionary.
- The dictionary stores each character as a key and its occurrence count as a value.

Example:

```python
{'a': 2, 'b': 2, 'c': 1}
```

### 4. First Loop – Frequency Counting

```python
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
```

- Iterates through every character in the original string.
- `frequency.get(char, 0)` retrieves the existing count.
- If the character doesn't exist, it returns `0`.
- `+ 1` increases the count.
- The updated value is stored in the dictionary.

Example:

For the input `"aabbc"`:

```python
{'a': 2, 'b': 2, 'c': 1}
```

### 5. Second Loop – Finding the Answer

```python
for char in text:
    if frequency[char] == 1:
        return char
```

- Iterates through the original string again.
- Checks each character's frequency.
- If the frequency is exactly `1`, it returns that character immediately.
- This preserves the original character order.

### 6. Return None

```python
return None
```

- Executes when no character appears exactly once.
- Returns `None` when every character is repeated.

### 7. Getting User Input

```python
text = input("Enter your text: ")
```

- Accepts a string from the user.
- Stores the input in the `text` variable.

### 8. Calling the Function

```python
result = first_non_repeating_character(text)
```

- Calls the function.
- Passes the input string as an argument.
- Stores the returned character or `None` in `result`.

### 9. Displaying the Result

```python
print(f"First non-repeating character: {result}")
```

- Displays the final result.
- Uses an f-string to insert the result into the output message.

## Expected Interaction

**Example 1**

```text
Enter your text: aabbcde
First non-repeating character: c
```

**Example 2**

```text
Enter your text: swiss
First non-repeating character: w
```

**Example 3**

```text
Enter your text: aabbcc
First non-repeating character: None
```

**Example 4**

```text
Enter your text:
First non-repeating character: None
```

## Test Cases

| Input | Expected Output |
|---|---|
| `"aabbcde"` | `"c"` |
| `"swiss"` | `"w"` |
| `"aabbcc"` | `None` |
| `"programming"` | `"p"` |
| `"aabbccd"` | `"d"` |
| `""` | `None` |

**Test Results:** 6/6 Passed

## Time and Space Complexity

### Time Complexity: O(n)

- The first loop traverses the string once: O(n).
- The second loop traverses the string once: O(n).
- Two linear traversals give O(n + n), which simplifies to O(n).

### Space Complexity: O(k)

- The dictionary stores the distinct characters.
- `k` represents the number of distinct characters in the string.
- Therefore, auxiliary space complexity is O(k).

## Key Concepts Learned

- Python Strings
- Dictionary data structures
- Dictionary `.get()` method
- Frequency counting
- Two-pass algorithms
- Return statements
- Time and space complexity
- Edge case handling

## What I Learned

In this challenge, I learned how to use Python dictionaries to count character frequencies efficiently.

I also understood why two separate loops are useful: the first loop calculates all character frequencies, while the second loop finds the first non-repeating character in the original order.

This challenge helped me improve my problem-solving skills and understand how to optimize a basic solution from O(n²) to O(n).

---

**Day 29 Completed!** 🚀

*100 Days, 100 Coding Challenges – Keep Learning, Keep Building!*