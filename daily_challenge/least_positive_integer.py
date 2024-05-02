"""
https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/?envType=daily-question&envId=2024-05-02
"""


def find_max_k(nums):
    # sorting the array to have the min (-ve) on the leftmost side
    # and the array to have the maz (+ve) on the rightmost side
    nums = sorted(nums)

    # two pointer approach, keeping the pointers
    start, end = 0, len(nums) - 1

    # while start is less than end
    while start < end:

        # edge case when after sorting the nums start and the end values are same
        # this means the entire array has the same value
        if nums[start] == nums[end]:
            return -1

        # if the start abs and end value are same i.r abs(-ve) == +ve
        if abs(nums[start]) == nums[end]:
            return abs(nums[start])

        # if the abs(+ve) > end, then we move the start pointer ahead
        if abs(nums[start]) > nums[end]:
            start += 1
        # else move the end pointer
        else:
            end -= 1

    return -1


nums = [-1, 2, -3, 3]
nums = [-104, -449, -318, -930, -195, 579, -410, 822, -814, -388, -863, 174, -814, 919, -877, 993, 741, 741, -623, -4,
        -4, 542, 997, 239, 447, -317, 409, -487, -34, 6, -914, 607, -622, 915, 573, 666, -229, 165, 841, -820, 703]

print(find_max_k(nums))
