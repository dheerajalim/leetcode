# similar to count occurrence of anagram, only difference is we append the index
def find_anagrams(string, pattern):
    hash_map = dict()
    n = len(string)
    k = len(pattern)

    for p in pattern:
        if p in hash_map:
            hash_map[p] += 1
        else:
            hash_map[p] = 1

    i, j = 0, 0
    pattern_count = len(hash_map)
    anagram_index = []

    while j < n:

        if string[j] in hash_map:
            hash_map[string[j]] -= 1
            if hash_map[string[j]] == 0:
                pattern_count -= 1

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:

            if pattern_count == 0:
                # in this question we append the starting index of sliding window which is ith index
                anagram_index.append(i)

            if string[i] in hash_map:
                hash_map[string[i]] += 1
                if hash_map[string[i]] == 1:
                    pattern_count += 1
            i += 1
            j += 1

    return anagram_index


s = "abab"
p = "ab"
print(find_anagrams(s, p))
