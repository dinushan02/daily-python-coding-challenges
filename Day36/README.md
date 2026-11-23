# Day 36 – Maximum Consecutive Ones

## Problem

Given a binary array `nums` containing only `0`s and `1`s, find the maximum number of consecutive `1`s in the array.

## Description

The goal is to find the longest continuous sequence of `1`s.

If a `0` appears, the current consecutive count resets to zero.

The function returns the highest consecutive count found in the array.

## Python Solution

```python
def find_max_consecutive_ones(nums):
    index = 0
    current_count = 0
    max_count = 0

    while index < len(nums):
        if nums[index] == 1:
            current_count += 1

            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0

        index += 1

    return max_count


nums = [1, 1, 0, 1, 1, 1]
result = find_max_consecutive_ones(nums)
print(result)
```

## Example

**Input:**
```text
[1, 1, 0, 1, 1, 1]
```

**Output:**
```text
3
```

**Explanation:**

The longest consecutive sequence of `1`s is `[1, 1, 1]`, which contains 3 elements.

## Test Cases

| No. | Input | Expected Output | Status |
|---|---|---:|---|
| 1 | `[1, 1, 0, 1, 1, 1]` | 3 | Passed |
| 2 | `[1, 0, 1, 1, 0, 1]` | 2 | Passed |
| 3 | `[0, 0, 0, 0]` | 0 | Passed |
| 4 | `[1, 1, 1, 1, 1]` | 5 | Passed |
| 5 | `[1]` | 1 | Passed |
| 6 | `[1, 1, 0, 1, 1, 1, 1]` | 4 | Passed |

**Testing Result:** All 6 test cases passed successfully.

## Approach

I used a single-pass array traversal approach with a `while` loop.

Three variables are used:

- `index`: Tracks the current array position.
- `current_count`: Counts consecutive `1`s.
- `max_count`: Stores the maximum consecutive count found so far.

### Algorithm

1. Initialize all three variables to zero.
2. Traverse the array using the `while` loop.
3. If the current element is `1`, increment `current_count`.
4. Update `max_count` if `current_count` is greater.
5. If the current element is `0`, reset `current_count` to zero.
6. Increment the index and continue until the array ends.
7. Return `max_count`.

## Complexity Analysis

- **Time Complexity:** O(n) – The array is traversed exactly once.
- **Space Complexity:** O(1) – Only a fixed number of variables are used.

## Concepts Learned

- Array Traversal
- While Loop
- Conditional Statements
- Counter Variables
- Maximum Value Tracking
- Single-Pass Algorithm
- Time and Space Complexity

## Key Takeaway

This challenge helped me understand how to count consecutive elements, reset counters when conditions change, and track maximum values efficiently using a single pass through an array.