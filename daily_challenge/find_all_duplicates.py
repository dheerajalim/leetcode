"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
"""

def find_duplicates(nums):

    result = []
    for i in range(len(nums)):
        # iterate through the elements of nums
        # and for the index at nums[i], if the value is -ve, then
        # this means that there is a another nums[i] which has same value
        # that's why a number is already negative
        # hence value at nums[i] is repeating
        if nums[abs(nums[i]) - 1] < 0:
            result.append(abs(nums[i]))
        # otherwise we go to the index at nums[i] and make it negative
        else:
            nums[abs(nums[i]) - 1] = -1 * nums[abs(nums[i]) - 1]

    return result

nums = [1]

print(find_duplicates(nums))
