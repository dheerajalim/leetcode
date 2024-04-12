def backtracking(nums, curr, curr_set, result):
    # if the len of curr == len of nums
    # then one of the permutation is achieved
    # add it to the result
    if len(curr) == len(nums):
        result.append(curr.copy())
        return

    # we iterate from the 0th index always
    # as we want the permutation with all the unused item in nums
    for i in range(len(nums)):
        # if the item is not already used in the permutation
        # then only we consider it
        if nums[i] not in curr_set:
            # add ti to the curr and the curr set
            curr.append(nums[i])
            curr_set.add(nums[i])
            # start backtracking
            backtracking(nums, curr, curr_set, result)
            # exclude the item from curr and curr_set
            curr.pop()
            curr_set.remove(nums[i])


def permutations(nums):
    # to store the result
    result = []
    # to store the current permutation array
    curr = []
    # to check if the item is already part of curr
    curr_set = set()

    backtracking(nums, curr, curr_set, result)

    return result


nums = [1, 2, 3]

print(permutations(nums))
