def backtracking(nums, idx, n, curr, result):
    # if the len of the curr is >= 2, then we add it to the result
    if len(curr) >= 2:
        # adding a copy of curr as we are passing curr as
        # reference
        result.append(curr.copy())

    # to store the items which are already included in a subsequence
    # example 4,6,7,7 => 4,6,7 and 4,6,7(last) are both same
    # so we need to maintain a set to see if the new item to include
    # also forms the same subsequence
    current_set = set()

    # iterate from the current position to the last item
    for i in range(idx, n):

        # if the curr is empty or the nums item is < curr last item and the item to
        # include is not already included then we add it to curr
        # then we look for next opportunity by calling backtracking recursively
        if (len(curr) == 0 or curr[-1] <= nums[i]) and nums[i] not in current_set:
            # include case
            curr.append(nums[i])
            # to add the item to the set to avoid duplicate subsequence
            current_set.add(nums[i])
            backtracking(nums, i + 1, n, curr, result)
            # exclude case: after this we call the next item,
            # which is the scenario where the i th index is excluded and i+1 is included
            curr.pop()


def find_subsequence(nums):
    # to store the result
    result = []
    # to store the current track subsequence
    curr = []

    # the nums length
    n = len(nums)
    # calling the backtracking from the first item in nums
    backtracking(nums, 0, n, curr, result)

    return result


nums = [4,6,7,7]
print(find_subsequence(nums))
