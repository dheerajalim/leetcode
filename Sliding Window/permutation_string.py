def check_inclusion(s1, s2):
    # get the length of the string
    n = len(s2)
    # get the length of the window / permutation string
    k = len(s1)

    # start from the 0th index
    i, j = 0, 0

    # to store the count of chars in the s1 string
    hash_map = {}

    # calculating the count of char in s1 string and
    # updating the hashmap
    for item in s1:

        if item in hash_map:
            hash_map[item] += 1
        else:
            hash_map[item] = 1

    # total count to maintain that the window still is not
    # what we need if >0 else == 0 then our window is valid and has the permutation
    total_count = len(hash_map)

    while j < n:
        # if the window size is less that or equal to
        # the required permutation, then we keep on
        # checking if the required permutation is achieved
        # by checking total_count and increment j to slide the window
        if j - i + 1 <= k:

            if s2[j] in hash_map:
                hash_map[s2[j]] -= 1
                if hash_map[s2[j]] == 0:
                    total_count -= 1

            j += 1

        # else if the window size crosses k, then we need
        # shrink the window by moving the ith index
        # and incrementing its value in hash map
        # as the item at ith position is no longer in
        # the sliding window
        else:
            if s2[i] in hash_map:
                hash_map[s2[i]] += 1
                if hash_map[s2[i]] == 1:
                    total_count += 1

            i += 1

        if total_count == 0:
            return True

    return False


s1 = "abc"
s2 = "dabcikl"

print(check_inclusion(s1, s2))
