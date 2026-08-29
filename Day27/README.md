# 🐍 Day 27: Remove Duplicates from a List

## 🧩 Problem Statement

Given a list of integers, create a new list containing only the **unique elements** while preserving their original order.

The program should:

* Accept a list of integers from the user.
* Identify duplicate numbers.
* Remove duplicate values.
* Preserve the original order.
* Display the list containing only unique numbers.

### 📌 Example

**Input:**

```text
10 20 10 30 20 40 30
```

**Output:**

```text
Unique numbers: [10, 20, 30, 40]
```

---

## 💡 Approach

The problem can be solved using a **list** and a **set**.

1. Get a list of integers from the user.
2. Create an empty list called `unique_numbers`.
3. Create an empty set called `seen`.
4. Loop through every number in the input list.
5. Check whether the number is already in `seen`.
6. If it is not present:

   * Add it to `unique_numbers`.
   * Add it to `seen`.
7. Return the list containing the unique numbers.

---

## 🧠 Logic

The main idea is to use:

```python
unique_numbers = []
seen = set()
```

The `unique_numbers` list stores the final result, while the `seen` set keeps track of values that have already been encountered.

For each number:

```python
if num not in seen:
    unique_numbers.append(num)
    seen.add(num)
```

If the number has not appeared before, it is added to both collections.

This allows us to remove duplicates while keeping the original order.

---

## 💻 Solution

```python
# Day 27: Remove Duplicates from a List


def remove_duplicates(numbers):

    unique_numbers = []
    seen = set()

    for num in numbers:
        if num not in seen:
            unique_numbers.append(num)
            seen.add(num)

    return unique_numbers


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = remove_duplicates(numbers)

print(f"Unique numbers: {result}")
```

---

## 📘 Key Python Concepts

### 📝 List

```python
unique_numbers = []
```

A list is used to store the unique numbers in their original order.

### 🔍 Set

```python
seen = set()
```

A set stores unique values and provides efficient membership checking.

### 🔄 For Loop

```python
for num in numbers:
```

The loop checks each number in the input list one by one.

### ✅ `in` Operator

```python
if num not in seen:
```

Checks whether the current number has already been encountered.

### ➕ `append()`

```python
unique_numbers.append(num)
```

Adds a new unique number to the result list.

---

## 🧪 Example 1

**Input:**

```text
10 20 10 30 20 40 30
```

**Output:**

```text
Unique numbers: [10, 20, 30, 40]
```

---

## 🧪 Example 2

**Input:**

```text
5 5 5 10 10 15
```

**Output:**

```text
Unique numbers: [5, 10, 15]
```

---

## 🧪 Example 3

**Input:**

```text
1 2 3 4 5
```

**Output:**

```text
Unique numbers: [1, 2, 3, 4, 5]
```

Since there are no duplicates, the original list remains unchanged.

---

## ⚡ Why Use a Set?

A beginner solution could use:

```python
if num not in unique_numbers:
```

However, searching through a list repeatedly can become slower as the input grows.

Using a set:

```python
seen = set()
```

allows much faster membership checking on average.

### Complexity

**Time Complexity:** `O(n)` on average

**Space Complexity:** `O(n)`

The program processes each input element once and uses additional space to store the unique values.

---

## 🎯 Learning Goal

The goal of this challenge is to understand how different Python data structures can work together.

In this problem:

**List** → preserves the order of the result.

**Set** → efficiently tracks values that have already appeared.

This is an important problem-solving pattern that can be useful in coding interviews and LeetCode-style challenges.

---

## 🧠 Interview-Style Thinking

Try solving the same problem without using `set()`.

Think about:

* How would you check for duplicates?
* What would happen if the list contains thousands of numbers?
* Which approach would be more efficient?
* Why is preserving the original order important?

---

## 🚀 Challenge Extension

Try modifying the function so that it:

* Works with strings instead of integers.
* Counts how many duplicates were removed.
* Returns both the unique list and the duplicate count.
* Handles an empty list.

---

## 📂 Project Structure

```text
Day27/
│
├── day27_remove_duplicates_from_list.py
└── README.md
```

---

## 🏁 Day 27 Completed

Another Python problem solved by focusing on **logic, data structures, and efficient problem solving**.

The goal is not just to write code that works, but to understand **why the solution works and how it can be improved**.
