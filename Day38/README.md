# Day 38 – Product of Array Except Self

## Problem Statement

Given an integer array `nums`, return an array `answer` such that:

`answer[i]` is equal to the product of all elements of `nums` except `nums[i]`.

**Requirements:**

- Do not use division.
- Solve the problem in O(n) time complexity.
- Aim for O(1) auxiliary space complexity, excluding the output array.
- Return a new output array.

## Example

**Input:**

```python
nums = [1, 2, 3, 4]
```

**Output:**

```python
[24, 12, 8, 6]
```

**Explanation:**

- Index 0: `2 × 3 × 4 = 24`
- Index 1: `1 × 3 × 4 = 12`
- Index 2: `1 × 2 × 4 = 8`
- Index 3: `1 × 2 × 3 = 6`

The product of all elements except the current element is calculated for every index.

---

## Python Solution

```python
def product_except_self(nums):
    array_length = len(nums)
    answer = [1] * array_length

    prefix_product = 1

    for index in range(array_length):
        answer[index] = prefix_product
        prefix_product *= nums[index]

    suffix_product = 1

    for index in range(array_length - 1, -1, -1):
        answer[index] *= suffix_product
        suffix_product *= nums[index]

    return answer


nums = [1, 2, 3, 4]
final_result = product_except_self(nums)
print(final_result)
```

**Output:**

```text
[24, 12, 8, 6]
```

---

## Step-by-Step Code Explanation

### Step 1 – Define the Function

```python
def product_except_self(nums):
```

Define a function named `product_except_self` that accepts an integer array called `nums`.

### Step 2 – Calculate the Array Length

```python
array_length = len(nums)
```

Use Python's built-in `len()` function to find the total number of elements.

For example:

```python
nums = [1, 2, 3, 4]
```

The array length is `4`.

### Step 3 – Initialize the Answer Array

```python
answer = [1] * array_length
```

Create a new list containing `1` for every position.

For our example:

```python
answer = [1, 1, 1, 1]
```

We use `1` because it is the multiplicative identity. Multiplying any number by `1` does not change its value.

### Step 4 – Initialize the Prefix Product

```python
prefix_product = 1
```

This variable stores the product of all elements before the current index.

Initially, it is `1` because there are no elements before the first index.

### Step 5 – Calculate Prefix Products

```python
for index in range(array_length):
    answer[index] = prefix_product
    prefix_product *= nums[index]
```

Traverse the array from left to right.

Two operations happen during each iteration:

1. Store the current prefix product in the answer array.
2. Multiply the running prefix product by the current element.

**Example:**

Input:

```python
[1, 2, 3, 4]
```

Prefix calculation:

| Index | Current Element | Prefix Product Stored | Updated Prefix |
|---|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 1 | 2 | 1 | 2 |
| 2 | 3 | 2 | 6 |
| 3 | 4 | 6 | 24 |

After the first loop:

```python
answer = [1, 1, 2, 6]
```

These values represent the products of all elements before each index.

### Step 6 – Initialize the Suffix Product

```python
suffix_product = 1
```

This variable stores the product of all elements after the current index.

We initialize it to `1` because there are no elements after the last index.

### Step 7 – Calculate Suffix Products

```python
for index in range(array_length - 1, -1, -1):
    answer[index] *= suffix_product
    suffix_product *= nums[index]
```

Traverse the array from right to left.

The `range()` function has three arguments:

```python
range(start, stop, step)
```

For this problem:

```python
range(array_length - 1, -1, -1)
```

It generates:

```text
3, 2, 1, 0
```

Two operations happen during each iteration:

1. Multiply the existing prefix product in `answer[index]` by the current suffix product.
2. Update the suffix product by multiplying it by the current array element.

**Example:**

Before the second loop:

```python
answer = [1, 1, 2, 6]
```

Suffix calculation:

| Index | Current Element | Suffix Product | Updated Answer |
|---|---:|---:|---:|
| 3 | 4 | 1 | 6 |
| 2 | 3 | 4 | 8 |
| 1 | 2 | 12 | 12 |
| 0 | 1 | 24 | 24 |

After the second loop:

```python
answer = [24, 12, 8, 6]
```

### Step 8 – Return the Final Result

```python
return answer
```

Return the completed output array.

### Step 9 – Call the Function

```python
nums = [1, 2, 3, 4]

final_result = product_except_self(nums)

print(final_result)
```

The function processes the input and returns:

```text
[24, 12, 8, 6]
```

---

## Understanding the Algorithm Visually

The algorithm works in two main passes.

**First Pass – Prefix Products (Left to Right)**

```text
Input:
[1, 2, 3, 4]

Prefix:
[1, 1, 2, 6]
```

**Second Pass – Suffix Products (Right to Left)**

The suffix products are calculated while updating the answer array.

```text
Prefix:
[1, 1, 2, 6]

Suffix:
[24, 12, 4, 1]

Final Answer:
[24, 12, 8, 6]
```

At every index:

`Answer[index] = Prefix Product × Suffix Product`

This produces the product of all elements except the current element.

---

## Test Cases

I tested the solution with 9 different test cases, including zeroes, negative numbers, repeated values, and edge cases.

| No. | Input | Expected Output | Status |
|---|---|---|---|
| 1 | `[1, 2, 3, 4]` | `[24, 12, 8, 6]` | Passed |
| 2 | `[-1, 1, 0, -3, 3]` | `[0, 0, 9, 0, 0]` | Passed |
| 3 | `[2, 3, 4, 5]` | `[60, 40, 30, 24]` | Passed |
| 4 | `[1, 1, 1, 1]` | `[1, 1, 1, 1]` | Passed |
| 5 | `[0, 2, 3, 4]` | `[24, 0, 0, 0]` | Passed |
| 6 | `[2, 0, 4, 0]` | `[0, 0, 0, 0]` | Passed |
| 7 | `[]` | `[]` | Passed |
| 8 | `[5]` | `[1]` | Passed |
| 9 | `[-2, -3, 4]` | `[-12, -8, 6]` | Passed |

**Testing Result: All 9 test cases passed successfully!**

---

## Complexity Analysis

### Time Complexity: O(n)

The algorithm traverses the input array twice:

- First traversal calculates prefix products.
- Second traversal calculates suffix products and updates the answer.

Therefore, the overall time complexity is O(n).

### Auxiliary Space Complexity: O(1)

The algorithm uses only a fixed number of additional variables:

- `array_length`
- `prefix_product`
- `suffix_product`
- `index`

The output array is excluded from auxiliary space complexity.

Therefore, auxiliary space complexity is O(1).

**Output Space Complexity: O(n)** because the returned answer array contains `n` elements.

---

## Concepts Learned

- Array Traversal
- Prefix Products
- Suffix Products
- Left-to-Right Traversal
- Right-to-Left Traversal
- Python `range()` Function
- List Initialization
- Running Product
- Space Optimization
- Handling Zeroes and Negative Numbers
- Time and Space Complexity

## Key Takeaway

This challenge helped me understand how prefix and suffix products work together to solve an array problem efficiently.

I first explored an approach using separate prefix and suffix lists. After understanding the logic, I improved the solution by reusing the output array to reduce auxiliary space.

The biggest lesson was that understanding the logic first makes optimization much easier.

**Understand the problem. Build the logic. Then optimize the solution.**

---

**Challenge:** 100 Days, 100 Coding Challenges

**Day:** 38

**Language:** Python

**Status:** Completed