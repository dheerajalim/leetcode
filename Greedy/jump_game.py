
def can_jump(nums):
    # edge case
    if nums[0] == 0:
        # if the first index is the end index as well
        # hence we need no jump
        if len(nums) == 1:
            return True
        # else we cannot jump any further, we return False
        return False

    # initialize the initial possible jump from the 0th index
    k = nums[0]

    # iterate over the available jumps
    for jump in nums:
        # if any point we have no available jumps, we cannot move ahead
        # return False
        if k < 0:
            return False
        # if at any point , we get more jump available
        # we update the available jumps
        if jump > k:
            k = jump
        # keep on decrementing the available jumps as we make a jump
        k -= 1

    return True


nums = [4, 3, 2, 2, 0, 5]
nums = [4, 3, 2, 3, 1, 0, 5]
nums = [4, 2, 2, 2, 0, 5]
nums = [3, 2, 1, 0, 4]
nums = [2, 3, 1, 1, 4]
# nums = [1, 3, 10, 1, 2, 1, 6]
# nums = [1,3,10,1,1,0,6]
# nums = [1,3,10,1,0,0,6]

print(can_jump(nums))
