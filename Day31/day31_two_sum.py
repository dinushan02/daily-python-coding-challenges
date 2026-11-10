def two_sum(nums, target):
    seen = {}

    for index, num in enumerate(nums):
        needed_number = target - num

        if needed_number in seen:
            return [seen[needed_number], index]

        seen[num] = index
        

nums = [-1, -2, -3, -4, -5]
target = -8

result = two_sum(nums, target)
print(result)
