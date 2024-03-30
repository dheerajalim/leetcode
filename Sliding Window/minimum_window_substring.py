def min_window(string, t):
    n = len(string)

    i, j = 0, 0
    # to store the start index of the min len window
    start_i = 0
    # to get the min length window
    window_size = float('inf')

    # to store the count of each item in the string t
    hash_map = {}
    for char in t:
        if char in hash_map:
            hash_map[char] += 1
        else:
            hash_map[char] = 1

    # this will be used to understand that the current window size
    # includes all the required characters present in string t
    # if this is 0, then the window is valid
    count_required = len(hash_map)

    # iterate till the last item of the string
    while j < n:
        # if the char in string is in hash map
        # then we reduce the value by 1
        # and if this value becomes 0, then we reduce
        # count_required as well
        if string[j] in hash_map:
            hash_map[string[j]] -= 1
            if hash_map[string[j]] == 0:
                count_required -= 1

        # if count_required == 0, this means the window which we have
        # has all the chars from  t. Hence we check its length
        # and store the min window length and if this is the smaller
        # window compared to prev window we found, then update the start_i index
        # once we get the window with count_required == 0, we try to check
        # by shrinking this window and see if the window size can
        # be further reduced
        while count_required == 0:

            current_size = j - i + 1
            if current_size < window_size:
                window_size = current_size
                start_i = i

            # also now when we move the ith index
            # we check if the char at  i index in string
            # is present in hash map, if yes we increment its
            # value in hashmap and if the value == 1, then
            # increment count_required by 1
            if string[i] in hash_map:
                hash_map[string[i]] += 1

                if hash_map[string[i]] == 1:
                    count_required += 1
            # slide the window from left
            i += 1

        # slide the window from right
        j += 1

    return string[start_i: start_i + window_size] if window_size != float('inf') else ""


s = "ADOBECODEBANC"
t = "ABC"
s = "a"
t = "aa"

print(min_window(s, t))
