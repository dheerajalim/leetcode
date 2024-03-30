def char_replacement(string, k):
    n = len(string)

    i, j = 0, 0
    # to store the frequency of each char
    # in the string
    hash_map = {}

    # default value for the max len
    max_len = float('-inf')

    while j < n:

        # if the item is already in the hash map, then we increment its count
        # else we add the item to hash map
        if string[j] in hash_map:
            hash_map[string[j]] += 1
        else:
            hash_map[string[j]] = 1

        # maintain the window size
        window_size = j - i + 1
        # after removing the max frequency item from the current window
        # the remaining value < =  k , this means the window is valid as
        # we need to replace <=k items and all items in the window will be
        # repeating, hence we update the max len
        if window_size - max(hash_map.values()) <= k:
            max_len = max(max_len, window_size)

        # after removing the max frequency item from the current window
        # the remaining value >  k , this means the window is invalid
        # as we have items that are non repeating > k, even if we replace all
        # upto k, then still the window will have not all repeating
        # hence we need to shrink
        elif window_size - max(hash_map.values()) > k:
            hash_map[string[i]] -= 1
            i += 1

        j += 1

    return max_len


s = "ABABBA"
k = 2
print(char_replacement(s, k))
