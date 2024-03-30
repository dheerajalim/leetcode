"""
To find all the possible subsets
"""


def subsets(nums):
    # the total possible subsets is equal to the 2 ^ n
    # where n is the length of nums
    n = len(nums)
    total_subsets = 1 << n  # this i equivalent to 2 ^ n

    # to store all the subsets
    ans = []

    # now we need to loop till total subsets, for example if n = 3
    # total subsets will be 8, so range will be 0 to 7, we will consider 0 as well
    for i in range(total_subsets):  # this start with 0

        # this list maintain the subset for the given item from range
        list = []

        # we iterate through the length of nums and
        # to check which bit is set, if it is set, we just add it to the subset list
        # the position which is set is the index in the nums which will be part of subset
        for j in range(n):
            if i & 1 << j:
                list.append(nums[j])

        # to store all the subsets
        ans.append(list)

    return ans


nums = [1, 4, 1]

print(subsets(nums))
