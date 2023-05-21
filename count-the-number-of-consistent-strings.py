def countConsistentStrings( allowed: str, words) -> int:
    # converting the allowed to dict
    temp_dict = {}
    consistent_count = 0
    for i in allowed:
        temp_dict[i] = 1
    ignore = False
    for word in words:
        ignore = False
        for char in word:
            if temp_dict.get(char) is None:
                ignore = True
                break
        if not ignore:
            consistent_count += 1

    return consistent_count


allowed = "ab"

words = ["ad","bd","aaab","baa","badab"]

print(countConsistentStrings(allowed,words))