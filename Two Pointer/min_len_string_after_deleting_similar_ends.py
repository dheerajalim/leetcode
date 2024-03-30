"""
https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/?envType=daily-question&envId=2024-03-05
"""


def minimum_length(s):
    # edge case
    # if the len of the string is 0
    if len(s) == 0:
        return 0
    # if there is only 1 element then we return 1
    # as prefix and suffix cannot be same index, hence it will not be able to remove
    if len(s) == 1:
        return 1

    # using two pointer approach
    # i, pointing to 0th index and j pointing to n-1 index
    i, j = 0, len(s) - 1

    # since i and j cannot be same prefixes as per the question
    # we iterate until i < j
    while i < j:
        # if the prefix and suffix are not equal
        # we return the length of the string
        if s[i] != s[j]:
            return (j - i) + 1

        # if the prefix and suffix are equal
        if s[i] == s[j]:
            # we move the i pointer upto the index where the
            # i and i+1 index values are same and i < j , as we do not want to
            # make the indices equal
            while i < j and s[i] == s[i + 1]:
                i += 1
            # similarly we move the jth index on the left until the values
            # are same
            while j > i and s[j] == s[j - 1]:
                j -= 1

            # if i and j both are same , this means we reached at a point where
            # all the prefix and suffix are same, so the entire string can be removed
            # example : "caabcaaccbac
            if i == j:
                return 0

        # this means the prefix and suffix upto i and j index were same
        # and we move i and j by 1 in right and left direction
        i += 1
        j -= 1

    # this is case when i == j and we moved out of the while loop
    # this means that i and j point to index which cannot be removed
    # hence the length will be 1
    # here bccb'cbc'bccbb, when we reach c, both i and j move to b
    # so the i == j and we move out of the loop and now we have b, which wil be of len 1
    # example : bccbcbcbccbb
    return 1


s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"

print(minimum_length(s))
