# def countKDifference(nums, k: int) -> int:
#     total = 0
#     for i in range(len(nums)):
#         valid_one = nums[i] - k
#         valid_two = nums[i] + k
#         temp = nums[i+1:]
#         total +=temp.count(valid_one)
#         total +=temp.count(valid_two)
#
#     return total


def countKDifference(nums, k: int) -> int:
    seen = dict()
    counter = 0
    for num in nums:
        tmp, tmp2 = num - k, num + k
        if tmp in seen:
            counter += seen[tmp]
        if tmp2 in seen:
            counter += seen[tmp2]

        if seen.get(num):
            seen[num] += 1
        else:
            seen[num] = 1

    return counter

x = [7,7,8,3,1,2,7,2,9,5]
# x = [1,2,2,1]
k = 6
print(countKDifference(x, k) )
# (7,1) = 7
# 7,1 = 7
# 8,2 =  8
# 8,2 = 8
# 3,9  = 3
# 1,7
