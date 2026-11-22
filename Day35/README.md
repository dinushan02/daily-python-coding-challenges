# Day 35 – Move Zeroes (Python)

## Problem

Given an integer list `nums`, move all zeroes to the end of the list while maintaining the relative order of all non-zero elements.

The operation must be performed in-place without creating another list.

## Description

The objective of this challenge is to move all zero values to the end of a list while keeping the original order of non-zero elements.

For example:

```python
nums = [0, 1, 0, 3, 12]
```

After moving all zeroes to the end:

```python
[1, 3, 12, 0, 0]
```

Instead of creating a new list, we can use two pointers to rearrange the elements in the original list.

## Approach – Two Pointers (Read/Write Technique)

This solution uses two pointers with different responsibilities.

### 1. Read Index

The `read_index` pointer traverses the entire list and checks each element.

### 2. Write Index

The `write_index` pointer tracks the position where the next non-zero element should be placed.

### Algorithm

1. Initialize both pointers at index `0`.
2. Traverse the list using `read_index`.
3. Check whether the current element is non-zero.
4. If it is non-zero, swap it with the element at `write_index`.
5. Increase `write_index` after placing the non-zero element.
6. Increase `read_index` to continue scanning.
7. Return the modified list.

## Python Concepts Practiced

1. Functions
2. Lists
3. Indexing
4. While loops
5. Conditional statements
6. Two Pointers technique
7. Read/Write Pointer technique
8. Tuple unpacking and swapping
9. In-place modification
10. Time and space complexity

## Python Code

```python
def move_zeroes(nums):
    write_index = 0
    read_index = 0

    while read_index < len(nums):
        if nums[read_index] != 0:
            nums[read_index], nums[write_index] = nums[write_index], nums[read_index]
            write_index += 1

        read_index += 1

    return nums


nums = [0, 1, 0, 3, 12]
result = move_zeroes(nums)
print(result)
```

## Expected Interaction

**Example 1:**

```text
Input:
[0, 1, 0, 3, 12]

Output:
[1, 3, 12, 0, 0]
```

**Example 2:**

```text
Input:
[0, 0, 1]

Output:
[1, 0, 0]
```

## Test Cases

All six test cases were executed successfully.

| Test | Input | Expected Output |
|---|---|---|
| 1 | `[0, 1, 0, 3, 12]` | `[1, 3, 12, 0, 0]` |
| 2 | `[0]` | `[0]` |
| 3 | `[1, 2, 3]` | `[1, 2, 3]` |
| 4 | `[0, 0, 1]` | `[1, 0, 0]` |
| 5 | `[1, 0, 2, 0, 3]` | `[1, 2, 3, 0, 0]` |
| 6 | `[0, 0, 0, 0]` | `[0, 0, 0, 0]` |

**Test Results: 6/6 Passed**

## Complexity Analysis

| Complexity | Value | Explanation |
|---|---|---|
| Time Complexity | O(n) | The read pointer traverses the list once. |
| Space Complexity | O(1) | The original list is modified directly without creating another list. |

## Key Takeaway

This challenge helped me understand how two pointers can work together with different responsibilities.

The `read_index` searches for non-zero elements, while the `write_index` tracks where those elements should be placed.

I also learned how to maintain the relative order of non-zero elements while modifying the original list in-place.

**One list, two pointers, and an efficient solution!**

---

**Challenge:** 100 Days, 100 Coding Challenges  
**Day:** 35  
**Language:** Python  
**Topic:** Lists & Two Pointers  
**Technique:** Read/Write Pointers  
**Status:** Completed