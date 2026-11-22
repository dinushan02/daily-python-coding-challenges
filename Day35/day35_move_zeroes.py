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