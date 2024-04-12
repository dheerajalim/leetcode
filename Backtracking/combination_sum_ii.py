def backtracking(candidates, target, idx, curr, result):
    # this is the base condition , if the sum of curr
    # becomes equal to target then we add the details to result
    if sum(curr) == target:
        result.append(curr.copy())
        return

    # we iterate over the items in the candidates
    for i in range(idx, len(candidates)):
        # this is a condition to avoid duplicate combinations
        # example if we have candidates like [1,1,2,5,6..]
        # in that case the second one should be ignored as
        # this will already be considered in the first 1 combination
        # i > idx is important to understand that we are considering the
        # index which is ahead of already processed similar value index
        if i > idx and candidates[i] == candidates[i - 1]:
            continue

        # this condition works when the sum with new candidate is already
        # exceeding the target , then we break as no sense of going ahead
        # as our array is already sorted
        if curr and (sum(curr) + candidates[i] > target):
            break

        # otherwise keep on forming the combination
        curr.append(candidates[i])
        # call the backtracking now
        backtracking(candidates, target, i + 1, curr, result)
        # exclude case
        curr.pop()


def combination_sum(candidates, target):
    result = []
    curr = []

    # this is sorted , so that when the sum goes beyond
    # target we can break and going ahead will only increase the sum
    candidates = sorted(candidates)
    backtracking(candidates, target, 0, curr, result)
    return result


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8

print(combination_sum(candidates, target))
