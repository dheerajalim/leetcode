def minOperations(nums) -> int:
    # [1,5,2,4,5] = 4
    # [1,5,6,4,5] = 4
    # [1,5,6,7,5] = 3
    # [1,5,6,7,8]=3

    # 5-2+1 = 4 [1,5,6,4,1]
    # 6-4+1 = 3 [1,5,6,7,1]
    # 7-1+1 = 7 [1,5,6,7,8]

    # compare a[i] , a[]i+1] , a[i+1] < a[i] : a[i+1] = a[i] - a[i+1] + 1
    min_operations = 0
    if len(nums) == 1:
        return min_operations

    for i in range(len(nums) - 1):
        if nums[i + 1] <= nums[i]:
            min_operations += nums[i] - nums[i + 1] + 1
            nums[i + 1] = nums[i + 1] + nums[i] - nums[i + 1] + 1

    return min_operations

inp = [1,5,2,4,1]

print(minOperations(inp))
