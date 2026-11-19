# Day 33 – Valid Palindrome (Python)

## Problem

Given a string `s`, determine whether it is a palindrome.

A palindrome is a string that reads the same forward and backward.

For this challenge:
- Convert uppercase letters into lowercase letters.
- Ignore all non-alphanumeric characters.
- Consider only letters (`a-z`) and numbers (`0-9`).

Return `True` if the string is a palindrome. Otherwise, return `False`.

## Description

The objective of this challenge is to check whether a given string reads the same forward and backward after removing spaces, punctuation, and other non-alphanumeric characters.

For example:

```python
s = "A man, a plan, a canal: Panama"
```

After converting to lowercase and ignoring non-alphanumeric characters:

```text
amanaplanacanalpanama
```

The cleaned string reads the same forward and backward.

**Output:**

```text
True
```

## Examples

**Example 1**

```python
Input: s = "A man, a plan, a canal: Panama"
Output: True
```

**Example 2**

```python
Input: s = "race a car"
Output: False
```

**Example 3**

```python
Input: s = " "
Output: True
```

## Approach – Two Pointers

The Two Pointers technique uses two variables to track positions in a string.

- The left pointer starts at the beginning of the string.
- The right pointer starts at the end of the string.
- Compare characters from both ends.
- Skip non-alphanumeric characters.
- Move both pointers towards the middle.
- If two characters don't match, return `False`.
- If all comparisons are successful, return `True`.

## Python Concepts Used

### 1. `lower()`

Converts all uppercase characters into lowercase characters.

```python
s = s.lower()
```

### 2. `isalnum()`

Checks whether a character is a letter or a number.

```python
s[left].isalnum()
```

Returns `True` for alphanumeric characters and `False` for spaces and punctuation.

### 3. Two Pointers

Uses two index variables to compare characters from opposite ends.

```python
left = 0
right = len(s) - 1
```

### 4. `continue`

Skips the current loop iteration and moves to the next iteration.

This helps skip unwanted characters without comparing them.

## Python Code

```python
def is_palindrome(s):
    s = s.lower()

    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue

        if not s[right].isalnum():
            right -= 1
            continue

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


s = "A man, a plan, a canal: Panama"
result = is_palindrome(s)
print(result)
```

## Expected Interaction

**Example 1:**

```text
Input:
A man, a plan, a canal: Panama

Output:
True
```

**Example 2:**

```text
Input:
race a car

Output:
False
```

## Test Cases

All six test cases were executed successfully.

| Test | Input | Expected Output |
|---|---|---|
| 1 | `"A man, a plan, a canal: Panama"` | `True` |
| 2 | `"race a car"` | `False` |
| 3 | `" "` | `True` |
| 4 | `"madam"` | `True` |
| 5 | `"12321"` | `True` |
| 6 | `"No lemon, no melon"` | `True` |

**Test Results: 6/6 Passed**

## Complexity Analysis

| Complexity | Value | Explanation |
|---|---|---|
| Time Complexity | O(n) | Each pointer moves through the string at most once. |
| Space Complexity | O(1) | Only two pointer variables are used. No additional data structure is created. |

## Key Takeaway

This challenge helped me understand how the Two Pointers technique works with strings.

Instead of creating another reversed or cleaned string, I used two pointers to compare characters directly from opposite ends.

I also practiced useful Python string methods such as `lower()` and `isalnum()`.

**Learning to solve problems efficiently is just as important as getting the correct output.**

---

**Challenge:** 100 Days, 100 Coding Challenges  
**Day:** 33  
**Language:** Python  
**Topic:** Strings & Two Pointers  
**Status:** Completed