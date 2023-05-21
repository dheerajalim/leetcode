def arrayPairSum( nums) -> int:
    # [1,2,2,5,6,6]
    # 1 + 2 + 6

    # [1,2,3,4]
    # 1 + 3

    # [2,4,8,15]
    # 2,8
    # Sort the array and then take pair of two with the min of them

    nums = sorted(nums)
    result = 0
    x = len(nums) - 1
    for i in range(0, len(nums) - 1, 2):
        result += nums[i]

    return result

nums  = [15,8,2,4]
print(arrayPairSum(nums))