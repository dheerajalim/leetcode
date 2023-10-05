"""
https://leetcode.com/problems/longest-common-prefix/

"""


def longestCommonPrefix(strs):

    # Solution 1
    """
    if len(strs) == 1:
        return strs[0]
    if len(strs) == 0:
        return ""

    prev = strs[0]

    for i in range(1, len(strs)):
        result = ""
        for j, k in zip(prev, strs[i]):
            if j == k:
                result += j
            else:
                break

        prev = result

    return result
    """

    # Solution 2:

    if len(strs) == 1:
        return strs[0]
    if len(strs) == 0:
        return ""

    # if we sort the array, then we can compare the first and last element for the common part and skip the ones in
    # between. ALso finding min and max in the strs works similar to sorted array

    first, last = min(strs), max(strs)
    result = ""
    for i in range(min(len(first), len(last))):

        if first[i] != last[i]:
            break

        result += first[i]

    return result

strs = ["flower", "flow", "flight"]
strs = ["dog", "racecar", "car"]
strs = ["dog"]
strs = ["cir", "car"]
print(longestCommonPrefix(strs))



