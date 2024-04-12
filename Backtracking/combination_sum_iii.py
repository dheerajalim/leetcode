def backtracking(nums, k, target, idx, curr, result):
    # base case is that we check if the sum(curr) is equal to target
    # and also that the len(curr) == k , this way we only consider k length answers
    if sum(curr) == target and len(curr) == k:
        result.append(curr.copy())

    # iterate through the items in nums
    for i in range(idx, len(nums)):
        # this condition checks if we are not proceeding the
        # required lenggth k and if the sum is already greater than target
        # then no need to call further ,as the nums is already in increasing order
        if curr and (len(curr) > k or sum(curr) + nums[i] > target):
            break
        # include the item
        curr.append(nums[i])
        # call backtracking
        backtracking(nums, k, target, i + 1, curr, result)
        # exclude the item
        curr.pop()


def combination_sum(k, n):
    # the n can range from i to 9, so this is
    # possible range of number which can form combination sum
    nums = [i for i in range(1, 10)]

    curr = []
    result = []
    target = n
    backtracking(nums, k, target, 0, curr, result)

    return result


k = 3
n = 7

print(combination_sum(k, n))
