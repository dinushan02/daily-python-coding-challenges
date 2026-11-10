# Day 31 – Two Sum (Python)

## Problem

Given an array of integers `nums` and an integer `target`, return the **indices of the two numbers** such that they add up to the target.

You may assume that each input has exactly one solution, and you cannot use the same element twice.

## Description

The goal of this challenge is to find two numbers in a list whose sum equals the given target and return their indices.

For example:

```python
nums = [2, 7, 11, 15]
target = 9
```

The numbers `2` and `7` add up to `9`.

- `2` is at index `0`.
- `7` is at index `1`.

**Output:**

```python
[0, 1]
```

## Approach 1 – Brute Force

The brute-force approach checks every possible pair of numbers using nested loops.

For each number, it compares that number with the remaining elements to find a pair whose sum equals the target.

### Complexity Analysis

- **Time Complexity:** O(n²) – Nested loops compare possible pairs.
- **Space Complexity:** O(1) – No additional data structure is required.

## Approach 2 – Optimized Solution Using Dictionary

Instead of checking every possible pair, we can use a Python dictionary to make the search more efficient.

### Key Concept

For each number, calculate the required number using:

```python
needed_number = target - num
```

Then check whether that required number already exists in the dictionary.

The dictionary stores:

- **Key:** Number
- **Value:** Index of that number

If the required number exists, return the two indices.

Otherwise, store the current number and its index in the dictionary.

### Python Code

```python
def two_sum(nums, target):
    # Dictionary to store numbers and their indices
    seen = {}

    # Iterate through the list with index and number
    for index, num in enumerate(nums):

        # Calculate the number needed to reach the target
        needed_number = target - num

        # Check whether the required number exists
        if needed_number in seen:

            # Return the previous index and current index
            return [seen[needed_number], index]

        # Store the current number and its index
        seen[num] = index


# Example input
nums = [2, 7, 11, 15]
target = 9

# Call the function
result = two_sum(nums, target)

# Display the result
print(result)
```

### Expected Interaction

**Example 1:**

```text
Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]
```

**Example 2:**

```text
Input:
nums = [3, 2, 4]
target = 6

Output:
[1, 2]
```

**Example 3:**

```text
Input:
nums = [3, 3]
target = 6

Output:
[0, 1]
```

## Test Cases

All six test cases were executed successfully.

| Test | Input | Target | Expected Output |
|---|---|---:|---|
| 1 | `[2, 7, 11, 15]` | 9 | `[0, 1]` |
| 2 | `[3, 2, 4]` | 6 | `[1, 2]` |
| 3 | `[3, 3]` | 6 | `[0, 1]` |
| 4 | `[1, 5, 8, 3]` | 11 | `[2, 3]` |
| 5 | `[4, 6, 10, 2]` | 8 | `[0, 3]` |
| 6 | `[-1, -2, -3, -4, -5]` | -8 | `[2, 4]` |

**Test Results: 6/6 Passed**

## Complexity Analysis – Optimized Approach

| Complexity | Value | Explanation |
|---|---|---|
| Time | O(n) | The list is traversed once, with average O(1) dictionary operations. |
| Space | O(n) | The dictionary may store up to n elements. |

## Python Concepts Practiced

1. Functions
2. Lists
3. Dictionaries
4. `enumerate()`
5. Conditional statements
6. Dictionary membership using `in`
7. Dictionary key-value pairs
8. Returning multiple indices
9. Time and space complexity
10. Hash map optimization

## Key Takeaway

The biggest lesson from this challenge is understanding how a dictionary can reduce the time required to search for a matching number.

Instead of checking every possible pair with nested loops, we can store previously visited numbers and find the required number in average O(1) lookup time.

**Brute Force: O(n²) → Optimized Dictionary: O(n)**

---

**Challenge:** 100 Days, 100 Coding Challenges  
**Day:** 31  
**Language:** Python  
**Topic:** Lists, Dictionaries & Hash Maps  
**Status:** Completed