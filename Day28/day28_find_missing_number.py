def find_missing_number(numbers):
    n = len(numbers)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)

    return expected_sum - actual_sum


numbers = [3, 0, 1]
result = find_missing_number(numbers)
print(f"Missing number: {result}")




