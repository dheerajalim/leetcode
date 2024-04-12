def backtracking(nums, idx, curr, result):
    # to append all the subsets to result
    result.append(curr.copy())

    for i in range(idx, len(nums)):
        # if the next element is same as previous element in
        # the same level, we would ignore as we need unique subsets
        # this is a condition to avoid duplicate combinations
        # example if we have candidates like [1,1,2,5,6..]
        # in that case the second one should be ignored as
        # this will already be considered in the first 1 combination
        # i > idx is important to understand that we are considering the
        # index which is ahead of already processed similar value index
        if i > idx and nums[i - 1] == nums[i]:
            continue
            
        curr.append(nums[i])

        backtracking(nums, i + 1, curr, result)

        curr.pop()


def subset_ii(nums):
    curr = []
    result = []
    # to have all the repeating elements together
    nums = sorted(nums)
    backtracking(nums, 0, curr, result)

    return result


nums = [1, 1, 2, 1]

print(subset_ii(nums))
