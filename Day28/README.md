# Day 28: Find the Missing Number

## Problem Description

Given a list containing `n` distinct numbers from the range `0` to `n`, find the one missing number.

The list contains exactly one missing number.

### Example 1

**Input:**
```python
numbers = [3, 0, 1]
```

**Output:**
```text
Missing number: 2
```

**Explanation:**

The complete range should be:

`[0, 1, 2, 3]`

But the given list is:

`[3, 0, 1]`

Therefore, the missing number is `2`.

### Example 2

**Input:**
```python
numbers = [0, 1]
```

**Output:**
```text
Missing number: 2
```

---

## Final Efficient Solution

```python
def find_missing_number(numbers):
    n = len(numbers)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)

    return expected_sum - actual_sum


numbers = [3, 0, 1]

result = find_missing_number(numbers)

print(f"Missing number: {result}")
```

**Output:**
```text
Missing number: 2
```

---

## Line-by-Line Explanation

### 1. Define the function

```python
def find_missing_number(numbers):
```

- Defines a function named `find_missing_number`.
- Accepts a list of numbers as an argument.
- The function will find and return the missing number.

### 2. Find the length of the list

```python
n = len(numbers)
```

- `len()` returns the number of elements in the list.
- We store that value in the variable `n`.

For example:

```python
numbers = [3, 0, 1]
n = 3
```

There are 3 elements, so `n = 3`.

### 3. Calculate the expected sum

```python
expected_sum = n * (n + 1) // 2
```

This is the mathematical formula for finding the sum of consecutive numbers from `0` to `n`.

**Formula:**

`n × (n + 1) ÷ 2`

For our example:

```python
n = 3

expected_sum = 3 * (3 + 1) // 2
expected_sum = 3 * 4 // 2
expected_sum = 12 // 2
expected_sum = 6
```

The complete range is:

`0 + 1 + 2 + 3 = 6`

Therefore, the expected sum is `6`.

**Why did I choose this formula?**

I noticed that the problem gives a continuous number range from `0` to `n`, with exactly one number missing.

Instead of checking every possible number one by one, I thought about calculating the total sum of the complete range.

The mathematical formula gives me that expected sum directly.

### 4. Calculate the actual sum

```python
actual_sum = sum(numbers)
```

- Python's built-in `sum()` function calculates the total of all numbers in the given list.
- We store the result in `actual_sum`.

For our example:

```python
numbers = [3, 0, 1]

actual_sum = 3 + 0 + 1
actual_sum = 4
```

### 5. Find and return the missing number

```python
return expected_sum - actual_sum
```

Now subtract the actual sum from the expected sum.

```python
expected_sum = 6
actual_sum = 4

missing_number = 6 - 4

return 2
```

The function returns `2`, which is the missing number.

### 6. Call the function

```python
numbers = [3, 0, 1]

result = find_missing_number(numbers)
```

- Creates the input list.
- Calls the function and passes the list.
- Stores the returned answer in `result`.

### 7. Display the result

```python
print(f"Missing number: {result}")
```

Uses an f-string to display the missing number.

Output:

```text
Missing number: 2
```

---

## How I Thought About This Problem

I didn't want to check every number individually if there was a simpler way.

My thinking process was:

**Step 1:** Understand the number range.

The numbers should be from `0` to `n`.

**Step 2:** Think about the complete range.

For `[3, 0, 1]`, the complete range is `[0, 1, 2, 3]`.

**Step 3:** Find a way to calculate the expected total.

I remembered the mathematical formula:

`n × (n + 1) ÷ 2`

**Step 4:** Compare the expected sum with the actual sum.

- Expected sum = `6`
- Actual sum = `4`

**Step 5:** Subtract the two values.

`6 - 4 = 2`

So, the missing number is `2`.

**My key idea:** Instead of searching for the missing number directly, I calculated the difference between the complete sum and the given list's sum.

---

## Why Use the Mathematical Formula?

There are different ways to solve this problem.

One approach is to convert the list into a set and check which number is missing.

However, the mathematical formula allows us to solve this problem without creating an additional set or another collection.

| Approach | Time Complexity | Extra Space |
|---|---|---|
| List checking | O(n²) | O(1) |
| Set approach | O(n) average | O(n) |
| Mathematical formula | O(n) | O(1) |

The mathematical approach is efficient because:

- It calculates the expected sum directly.
- It uses Python's built-in `sum()` function to calculate the actual sum.
- It does not create an additional data structure.

---

## Time and Space Complexity

### Time Complexity: O(n)

Why?

- `len(numbers)` takes O(1) time.
- Calculating the expected sum takes O(1) time.
- `sum(numbers)` visits each element once, taking O(n) time.
- Subtraction takes O(1) time.

Therefore, the overall time complexity is:

**O(n)**

### Space Complexity: O(1)

Why?

- We only use a few variables: `n`, `expected_sum`, and `actual_sum`.
- We do not create another list or set.
- The extra space does not grow with the input size.

Therefore, the auxiliary space complexity is:

**O(1)**

---

## Important Note

This solution works under the problem's assumptions:

- The numbers are distinct.
- The numbers belong to the range `0` to `n`.
- Exactly one number is missing.

If these conditions are not satisfied, this formula may not give the correct answer.

---

## What I Learned

- How to identify mathematical patterns in programming problems.
- How to use Python's built-in `sum()` function.
- How to calculate the sum of consecutive numbers.
- How to improve a solution by avoiding unnecessary data structures.
- How to analyse time and space complexity.
- How mathematical thinking can help solve coding problems efficiently.

**Day 28 completed: Find the Missing Number using a mathematical formula.**