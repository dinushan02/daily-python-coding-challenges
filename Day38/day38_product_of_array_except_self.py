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