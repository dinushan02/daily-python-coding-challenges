# Day 32 – Contains Duplicate (Python)

## Problem

Given an integer list `nums`, return `True` if any value appears at least twice in the list.

Return `False` if every element is unique.

## Description

The objective of this challenge is to identify whether a list contains duplicate elements.

Instead of comparing every element with every other element, we can use Python's built-in `set` data structure.

A set automatically stores only unique values.

By comparing the length of the original list with the length of the set, we can determine whether duplicates exist.

## Examples

**Example 1**

```python
Input: nums = [1, 2, 3, 1]
Output: True
```

**Example 2**

```python
Input: nums = [1, 2, 3, 4]
Output: False
```

**Example 3**

```python
Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: True
```

## Approach – Using Python Set

### Key Concept

Python sets automatically remove duplicate values.

For example:

```python
nums = [1, 2, 3, 1]

unique_set = set(nums)

print(unique_set)
```

Output:

```text
{1, 2, 3}
```

The original list contains 4 elements, while the set contains only 3 unique elements.

Therefore, if the lengths are different, the list contains duplicates.

### Logic

1. Convert the original list into a set.
2. Compare the length of the original list with the length of the set.
3. If the lengths are different, return `True`.
4. Otherwise, return `False`.

## Python Code

```python
def contains_duplicate(nums):
    # Convert the list into a set to remove duplicates
    unique_set = set(nums)

    # Compare the lengths to detect duplicate values
    return len(nums) != len(unique_set)


# Example input
nums = [1, 2, 3, 1]

# Call the function
result = contains_duplicate(nums)

# Display the result
print(result)
```

## Line-by-Line Explanation

**1. Define the function**

```python
def contains_duplicate(nums):
```

Creates a function that accepts a list of integers.

**2. Convert the list into a set**

```python
unique_set = set(nums)
```

Creates a set containing only unique values. Duplicate elements are automatically removed.

**3. Compare the lengths**

```python
return len(nums) != len(unique_set)
```

- If the lengths are different, duplicates exist, so the result is `True`.
- If the lengths are equal, all elements are unique, so the result is `False`.

## Expected Interaction

**Example 1:**

```text
Input:
nums = [1, 2, 3, 1]

Output:
True
```

**Example 2:**

```text
Input:
nums = [1, 2, 3, 4]

Output:
False
```

## Test Cases

All six test cases were executed successfully.

| Test | Input | Expected Output |
|---|---|---|
| 1 | `[1, 2, 3, 1]` | `True` |
| 2 | `[1, 2, 3, 4]` | `False` |
| 3 | `[1, 1, 1]` | `True` |
| 4 | `[]` | `False` |
| 5 | `[5]` | `False` |
| 6 | `[-1, -2, -3, -1]` | `True` |

**Test Results: 6/6 Passed**

## Complexity Analysis

| Complexity | Value | Explanation |
|---|---|---|
| Time Complexity | O(n) average | Converting the list into a set takes O(n) average time. |
| Space Complexity | O(n) | The set may store up to n unique elements. |

## Python Concepts Practiced

1. Functions
2. Lists
3. Sets
4. Type conversion
5. `set()` built-in function
6. `len()` built-in function
7. Comparison operators
8. Boolean return values
9. Time and space complexity

## Key Takeaway

One important lesson from this challenge is understanding how Python sets handle duplicate values automatically.

Instead of writing nested loops to compare every element, we can use a set and compare the lengths to detect duplicates efficiently.

**A simple Python set can make duplicate detection much easier!**

---

**Challenge:** 100 Days, 100 Coding Challenges  
**Day:** 32  
**Language:** Python  
**Topic:** Lists & Sets  
**Status:** Completed