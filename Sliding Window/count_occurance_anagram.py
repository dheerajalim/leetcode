def count_anagram(txt, pattern):
    # create a hashmap with count of each occurance of
    # word in the pattern
    hash_map = dict()
    for p in pattern:

        if hash_map.get(p):
            hash_map[p] += 1
        else:
            hash_map[p] = 1

    # starting the sliding window process
    i, j = 0, 0
    n = len(txt)
    # window size is the size of the pattern
    k = len(pattern)

    # keep the pattern count, decrement this value by 1 if any of the key's value becomes 0
    pattern_count = len(hash_map)
    # anagram count
    count = 0

    while j < n:

        if txt[j] in hash_map:
            hash_map[txt[j]] -= 1
            if hash_map[txt[j]] == 0:
                pattern_count -= 1

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:

            if pattern_count == 0:
                count += 1

            # update the count of the character at i position
            # as now this is moving out of the window, we increase its count
            if txt[i] in hash_map:
                hash_map[txt[i]] += 1
                # if the count of the character is back to 1, then we increment the patter_count
                if hash_map[txt[i]] == 1:
                    pattern_count += 1

            i += 1
            j += 1

    return count
# txt = 'forxxorfxdofr'
# pat = 'for'
txt = "aabaabaa"
pat = "aaba"

print(count_anagram(txt, pat))