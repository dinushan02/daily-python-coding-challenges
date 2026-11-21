# Day 34 – Reverse String (Python)

## Problem

Write a function that reverses a list of characters.

The reversal must be performed in-place, meaning you must modify the original list without creating another list.

## Description

The objective of this challenge is to reverse the order of characters in a list.

Instead of creating a new reversed list, we can use the Two Pointers technique to swap elements from opposite ends.

For example:

```python
s = ["h", "e", "l", "l", "o"]
```

After reversing:

```python
["o", "l", "l", "e", "h"]
```

## Examples

**Example 1**

```python
Input: s = ["h", "e", "l", "l", "o"]
Output: ["o", "l", "l", "e", "h"]
```

**Example 2**

```python
Input: s = ["H", "a", "n", "n", "a", "h"]
Output: ["h", "a", "n", "n", "a", "H"]
```

## Approach – Two Pointers

The Two Pointers technique uses two variables to track positions in a list.

- The left pointer starts at index `0`.
- The right pointer starts at the last index.
- Swap the elements at both pointer positions.
- Move the left pointer forward.
- Move the right pointer backward.
- Continue until both pointers meet or cross.

This approach reverses the list in-place.

## Python Concepts Practiced

### 1. Lists

A Python list stores multiple elements in an ordered collection.

```python
s = ["h", "e", "l", "l", "o"]
```

### 2. Indexing

Access list elements using their positions.

```python
s[left]
s[right]
```

### 3. Two Pointers

Use two variables to track positions from opposite ends.

```python
left = 0
right = len(s) - 1
```

### 4. Swapping Elements

Python allows two values to be swapped in a single statement.

```python
s[left], s[right] = s[right], s[left]
```

### 5. In-Place Modification

The original list is modified directly without creating another list.

## Python Code

```python
def reverse_string(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1

    return s


s = ["h", "e", "l", "l", "o"]
result = reverse_string(s)
print(result)
```

## Expected Interaction

**Example 1:**

```text
Input:
["h", "e", "l", "l", "o"]

Output:
["o", "l", "l", "e", "h"]
```

**Example 2:**

```text
Input:
["H", "a", "n", "n", "a", "h"]

Output:
["h", "a", "n", "n", "a", "H"]
```

## Test Cases

All six test cases were executed successfully.

| Test | Input | Expected Output |
|---|---|---|
| 1 | `["h", "e", "l", "l", "o"]` | `["o", "l", "l", "e", "h"]` |
| 2 | `["H", "a", "n", "n", "a", "h"]` | `["h", "a", "n", "n", "a", "H"]` |
| 3 | `["a"]` | `["a"]` |
| 4 | `["a", "b"]` | `["b", "a"]` |
| 5 | `["1", "2", "3", "4"]` | `["4", "3", "2", "1"]` |
| 6 | `[]` | `[]` |

**Test Results: 6/6 Passed**

## Complexity Analysis

| Complexity | Value | Explanation |
|---|---|---|
| Time Complexity | O(n) | Each pointer moves towards the middle, so the list is traversed in linear time. |
| Space Complexity | O(1) | The reversal happens in-place without creating another list. |

## Key Takeaway

This challenge helped me practice the Two Pointers technique in a different way.

In Day 33, I used two pointers to compare characters from opposite ends of a string.

In Day 34, I used the same technique to swap elements and reverse a list in-place.

One technique, different problem-solving applications!

---

**Challenge:** 100 Days, 100 Coding Challenges  
**Day:** 34  
**Language:** Python  
**Topic:** Lists & Two Pointers  
**Status:** Completed