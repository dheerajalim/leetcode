"""
https://leetcode.com/problems/find-the-duplicate-number/description/
"""

def find_duplicate(nums):

    nums = sorted(nums)

    for i in range(1, len(nums)):

        if nums[i-1] == nums[i]:
            return nums[i]




nums =[7,9,7,4,2,8,7,7,1,5]

print(find_duplicate(nums))