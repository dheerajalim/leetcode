"""
https://leetcode.com/problems/first-missing-positive/description/?envType=daily-question&envId=2024-03-26
"""


# this is Using O(n) Space
def find_missing_positive(nums) -> int:
    # we need only the numbers taht are >0
    # hence we iterate over the nums and add all the numbers >0
    # to a set
    nums_set = set()
    for i in nums:
        if i > 0:
            nums_set.add(i)

    # now we iterate from 1 to 2**31-1 (this is the given max length)
    # and see if there is any missing i in the nums set, if yes we return that
    for i in range(1, (1 << 31) - 1):
        if i not in nums_set:
            return i


# we need to solve this is in O(1) space
# solution 2:

def find_missing_positive_space(nums) -> int:
    # first we iterate and check if the nums contain 1
    contains_one = False
    for i in range(len(nums)):
        if nums[i] == 1:
            contains_one = True
        # we also replace all negative numbers with 1
        # as we need to avoid negative numbers and if we replace with 1,
        # index will be 0, which is reachable
        if nums[i] <= 0 or nums[i] > len(nums):
            nums[i] = 1

    # if we do not find 1, then it is obvious that it will be the smallest positive integer that we need
    if not contains_one:
        return 1

    # we iterate over nums and then check the value at index i
    # this value will serve as index for us, we got to the index equal to this value
    # and see if it is +ve, mark it -ve else continue
    # this allows us to understand that these positions are already visisted
    for i in range(len(nums)):

        if nums[abs(nums[i]) - 1] > 0:
            nums[abs(nums[i]) - 1] = -1 * nums[abs(nums[i]) - 1]
        else:
            continue

    # we iterate again over nums and see which index value is positive
    # if it is positive that means this index value was never visisted and the
    # index + 1 is the result
    for i in range(len(nums)):
        if nums[i] > 0:
            return i + 1

    return len(nums) + 1


nums = [1]

print(find_missing_positive_space(nums))
