def backtracking(nums, idx, curr, result):
    # to append the current subarray to the result
    result.append(curr.copy())

    # iterate over all the items in nums
    for i in range(idx, len(nums)):
        # all items are unique in nums, so we need not worry about maintaining a set
        # add the item to curr list to get subarray
        curr.append(nums[i])
        # call backtracking with the next available item in nums
        backtracking(nums, i + 1, curr, result)
        # after this run the exclude process of backtracking
        curr.pop()


def subsets(nums):
    # store the final result
    result = []
    # store the current recursion result
    curr = []

    backtracking(nums, 0, curr, result)

    return result


nums = [1, 2, 3]

print(subsets(nums))
