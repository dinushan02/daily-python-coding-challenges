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
