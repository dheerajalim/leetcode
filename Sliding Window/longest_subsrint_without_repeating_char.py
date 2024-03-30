def longest_substr(string):
    n = len(string)

    i, j = 0, 0
    # store the count of the char in the hash map as the value
    hash_map = {}
    max_len = 0

    # iterate until the last character
    while j < n:

        # if the char is already in the hash map
        # this means this is a duplicate char in the window
        # hence we keep on moving the ith index(slide window - > Shrink)
        # until the count of string[j] does not become 1, which means we slided
        # the window such that the duplicate item is now not part of the window anymore
        if string[j] in hash_map:
            # the element count is increased,which makes sure that it is
            # occuring more than once
            hash_map[string[j]] += 1
            # update the position of i, sliding the window
            # until the item string[j] is not reduce to 1 back
            while hash_map[string[j]] > 1:
                hash_map[string[i]] -= 1
                i += 1

        # if the item is not found in the window
        # then this is non-duplicate item and hence this will  be added
        # to the hash map
        else:
            hash_map[string[j]] = 1

        # return the longest substring
        max_len = max(max_len, j - i + 1)

        j += 1

    return max_len


s = "abbbacderfaabaab"
# s = "abbbacderfazxlopcghijkl"
# s = "abcabcbb"

print(longest_substr(s))
