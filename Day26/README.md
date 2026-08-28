# 🐍 Day 26: Second Largest Unique Number

## 🧩 Problem Statement

Given a list of integers, find the **second largest unique number** in the list.

The program should:

* Accept a list of integers from the user.
* Remove duplicate numbers.
* Find the largest unique number.
* Find the second largest unique number.
* Handle the case where fewer than two unique numbers exist.

### 📌 Example

**Input:**

```text
10 5 8 20 15 20 10
```

**Unique Numbers:**

```text
[10, 5, 8, 20, 15]
```

**Output:**

```text
Second largest: 15
```

---

## 💡 Approach

The problem can be solved using the following steps:

1. Get a list of integers from the user.
2. Create an empty list to store unique numbers.
3. Loop through the original list.
4. Add a number to the unique list only if it is not already present.
5. Check whether there are at least two unique numbers.
6. Keep track of the largest and second largest numbers.
7. Compare each number and update the values when necessary.
8. Return the second largest unique number.

---

## 🧠 Logic

The main logic is based on comparing numbers while keeping track of two values:

```text
largest
second_largest
```

When a number larger than `largest` is found:

```text
second_largest = largest
largest = number
```

Otherwise, if the number is greater than `second_largest`, it becomes the new second largest.

This allows the program to find the answer without using:

```python
max()
sort()
sorted()
```

---

## 💻 Concepts Practiced

This challenge combines several Python fundamentals:

* 📝 Lists
* 🔄 `for` loops
* 🔀 `if-elif-else`
* ⚖️ Comparison operators
* 🧩 Functions
* 🔢 `len()`
* 🗺️ `map()`
* ✂️ `split()`
* ⌨️ User input
* 🔍 Duplicate checking
* 🧠 Logical problem solving

---

## 🔍 Important Python Concepts

### `map()`

```python
map(int, input().split())
```

Converts each value entered by the user into an integer.

### `split()`

```python
input().split()
```

Separates the user's input into individual values.

For example:

```text
10 5 8 20
```

becomes:

```python
["10", "5", "8", "20"]
```

### `list()`

```python
list(map(int, input().split()))
```

Converts the mapped values into a Python list.

---

## 🧪 Example 1

**Input:**

```text
10 5 8 20 15 20 10
```

**Output:**

```text
Second largest: 15
```

---

## 🧪 Example 2

**Input:**

```text
50 20 40 50 30
```

After removing duplicates:

```text
[50, 20, 40, 30]
```

**Output:**

```text
Second largest: 40
```

---

## ⚠️ Example 3: No Second Largest Number

**Input:**

```text
5 5 5
```

There is only one unique number.

**Output:**

```text
No second largest number exists.
```

---

## 🎯 Learning Goal

The goal of this challenge is not just to get the correct answer.

It is to practice breaking a programming problem into smaller steps and solving it using fundamental Python concepts.

This challenge also introduces the idea of writing reusable logic inside a function.

---

## 🚀 Challenge Extension

After solving this problem, try improving your solution by thinking about:

* How would you handle an empty list?
* Can you solve it using a `set`?
* Can you find the answer without creating a separate unique list?
* What would be the time complexity of your solution?

These extensions can help develop stronger problem-solving skills for coding interviews and platforms such as LeetCode.

---

## 📂 Project Structure

```text
Day26/
│
├── day26_second_largest_unique.py
└── README.md
```

---

## 🏁 Day 26 Completed

Another problem solved using Python fundamentals. 🐍

The focus of this challenge is **logical thinking, clean code, and understanding the problem before writing the solution.**
