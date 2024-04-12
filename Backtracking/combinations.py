"""
https://leetcode.com/problems/combinations/description/
"""


def backtracking(arr, idx, k, curr, result):
    # base Case : If the length of curr == k
    # this means the required sized combination is found
    # we add it to the result and return
    if len(curr) == k:
        result.append(curr.copy())
        return

    # we keep on exploring all the items in arr
    for i in range(idx, len(arr)):
        # once we include
        curr.append(arr[i])
        # the explore after including
        backtracking(arr, i + 1, k, curr, result)
        # then we exclude and explore after excluding
        curr.pop()


def combine(n, k):
    # the list of n items from 1 to n
    arr = [i for i in range(1, n + 1)]
    # to store the combinations
    result = []
    # to store the combination in the current exploration path
    curr = []
    backtracking(arr, 0, k, curr, result)

    return result


n = 4
k = 2

print(combine(n, k))
