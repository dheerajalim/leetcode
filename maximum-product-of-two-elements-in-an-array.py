def maxProduct(nums) -> int:
    # can sort and take the last two values as they can be the max possible ones
    # nums = sorted(nums)

    # result = (nums[-1] -1) * (nums[-2] -1)
    # return result

    # approach second: finding the two max elements by iterating

    max_1 = nums[0]
    max_2 = nums[1]

    if len(nums) > 2:
        for i in range(2, len(nums)):

            if max_1 <= max_2 and nums[i] > max_1:
                max_1 = nums[i]
            elif max_1 >= max_2 and nums[i] > max_2:
                max_2 = nums[i]
    print
    result = (max_1 - 1) * (max_2 - 1)
    return result

x = [9,2,3,5,2,6,9,7,9,4,5,5,10,8,9]
print(maxProduct(x))