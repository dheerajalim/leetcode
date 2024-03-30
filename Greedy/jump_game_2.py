def can_jump(nums):
    # edge case
    # if the first position is 0, then you cannot reach the end
    if len(nums) == 0:
        return 0

    # maintain the left and right position
    # this helps us to calculate the range
    l, r = 0, 0
    # the result to be stored to get the min steps
    res = 0
    # to maintian the farthest point that can be reached
    farthest = 0

    # iterate until the right value of range is less than the
    # total number of indexes
    while r < len(nums) - 1:
        # we will check the farthest point that we can reach
        # in the given range and accordingly update the farthest point
        for i in range(l, r + 1):
            farthest = max(farthest, nums[i] + i)

        # once we get the farthest point in the range
        # we update the left as right + 1 and right as farthest
        l = r + 1
        r = farthest
        # counts the number of ranges that we made.
        # this is the result
        res += 1

    return res


nums = [4, 3, 2, 2, 0, 5]
nums = [4, 3, 2, 3, 1, 0, 5]
nums = [4, 2, 2, 2, 0, 5]
nums = [3, 2, 1, 0, 4]
nums = [2, 3, 1, 1, 4]
# nums = [1, 3, 10, 1, 2, 1, 6]
# nums = [1,3,10,1,1,0,6]
# nums = [1,3,10,1,0,0,6]

print(can_jump(nums))
