def contains_duplicate(nums):
    unique_set = set(nums)
    return len(nums) != len(unique_set)


nums = 	[-1, -2, -3, -1]
result = contains_duplicate(nums)
print(result)

