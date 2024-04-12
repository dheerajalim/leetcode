def backtracking(candidates, target, idx, curr, result):
    # the base case, where if the sum is == target, then this is a valid combination
    if sum(curr) == target:
        result.append(curr.copy())
        return

    # keep on iterating in the items of candidates
    for i in range(idx, len(candidates)):
        # this condition checks if we add candidates[i] to curr, will it be still <= target
        # if not , then we basically break as going ahead makes no sense
        if curr and (sum(curr) + candidates[i] > target):
            break

        # we update the curr otherwise as adding ith item is still <= target
        curr.append(candidates[i])

        # call the backtracking function, please note the idx here is i
        # this is because we want to check the combinations from current
        # position, and we do not want to check with the previous position as '
        # those combinations would have been taken care when i was at i-1 position
        # so we always want to check the combinations from ith position and not from i = 0 position
        backtracking(candidates, target, i, curr, result)

        # the exclude case of backtracking
        curr.pop()


def combination_sum(candidates, target):
    result = []
    curr = []

    # this is sorted , so that when the sum goes beyond
    # target we can break and going ahead will only increase the sum
    candidates = sorted(candidates)
    backtracking(candidates, target, 0, curr, result)
    return result


candidates = [2, 3, 6, 7]
candidates = [1, 2, 3]
target = 4

print(combination_sum(candidates, target))
