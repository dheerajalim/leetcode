"""
https://leetcode.com/problems/squares-of-a-sorted-array/?envType=daily-question&envId=2024-03-02

since the first and the last element in the array can be the potential maximum
numbers after making the square, hence we fill the result array backwards
"""


def sortedSquares(nums):
    i, j = 0, len(nums) - 1
    res = [0] * len(nums)
    pos = len(nums) - 1
    while pos >= 0:

        a, b = nums[i] ** 2, nums[j] ** 2

        if a > b:
            res[pos] = a
            i += 1

        else:
            res[pos] = b
            j -= 1

        pos -= 1

    return res


nums = [-4, -1, 0, 3, 10]
nums = [-7, -3, 2, 3, 11]
nums = [-5, -3, -2, -1]
nums = [-10000, -9999, -7, -5, 0, 0, 10000]
# nums = [-2, 0]

print(sortedSquares(nums))
