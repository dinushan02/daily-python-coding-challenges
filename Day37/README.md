# Day 37 – Best Time to Buy and Sell Stock

## Problem

You are given an array `prices` where `prices[i]` represents the price of a stock on the `i-th` day.

You can buy the stock on one day and sell it on a later day.

Your task is to find the maximum profit you can achieve.

If no profitable transaction is possible, return `0`.

## Python Solution

```python
def max_profit(prices):
    if not prices:
        return 0

    index = 0
    minimum_price = prices[0]
    maximum_profit = 0

    while index < len(prices):
        if minimum_price > prices[index]:
            minimum_price = prices[index]

        possible_profit = prices[index] - minimum_price

        if possible_profit > maximum_profit:
            maximum_profit = possible_profit

        index += 1

    return maximum_profit


prices = [7, 1, 5, 3, 6, 4]
result = max_profit(prices)
print(result)
```

## Example

**Input:**

```text
[7, 1, 5, 3, 6, 4]
```

**Output:**

```text
5
```

**Explanation:**

- Buy the stock at price `1`.
- Sell the stock at price `6`.
- Maximum profit = `6 - 1 = 5`.

The buying day must always come before the selling day.

## Approach

I used a single-pass traversal approach with a `while` loop and the Greedy Algorithm.

The solution uses three variables:

- `index`: Tracks the current position in the array.
- `minimum_price`: Stores the lowest stock price found so far.
- `maximum_profit`: Stores the highest profit found so far.

I also used `possible_profit` to calculate the profit for each day's stock price.

### Algorithm

1. Check whether the input list is empty. If it is, return `0`.
2. Initialize `minimum_price` with the first stock price.
3. Traverse the array using a `while` loop.
4. If today's price is lower than `minimum_price`, update it.
5. Calculate today's possible profit by subtracting the minimum price from today's price.
6. If today's possible profit is greater than `maximum_profit`, update it.
7. Continue until all prices have been checked.
8. Return the maximum profit.

## Test Cases

| No. | Input | Expected Output | Status |
|---|---|---:|---|
| 1 | `[7, 1, 5, 3, 6, 4]` | 5 | Passed |
| 2 | `[7, 6, 4, 3, 1]` | 0 | Passed |
| 3 | `[2, 4, 1]` | 2 | Passed |
| 4 | `[1, 2, 3, 4, 5]` | 4 | Passed |
| 5 | `[3, 3, 3, 3]` | 0 | Passed |
| 6 | `[5, 2, 8, 1, 9]` | 7 | Passed |
| 7 | `[]` | 0 | Passed |
| 8 | `[5]` | 0 | Passed |
| 9 | `[1, 5]` | 4 | Passed |

**Testing Result: All 9 test cases passed successfully!**

## Complexity Analysis

- **Time Complexity: O(n)** – The array is traversed exactly once.
- **Space Complexity: O(1)** – Only a fixed number of variables are used.

## Concepts Learned

- Array Traversal
- While Loop
- Greedy Algorithm
- Minimum Value Tracking
- Maximum Profit Tracking
- Conditional Statements
- Edge Case Handling
- Time and Space Complexity

## Key Takeaway

This challenge helped me understand how to track the minimum value and maintain the maximum result while traversing an array.

I also learned that we don't always need nested loops to solve an optimization problem. A single traversal can be enough when we maintain the right information.

Another important lesson was handling edge cases, such as an empty input list.