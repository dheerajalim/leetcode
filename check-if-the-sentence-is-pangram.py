def checkIfPangram(sentence: str) -> bool:
    # creating a dict with all alphabates
    # then after checking the sentence if the sum of values of the dict is 26
    # then this is pangram

    all_alpha = dict()

    for i in range(97, 123):
        all_alpha[chr(i)] = 0

    for j in sentence:
        if all_alpha.get(j):
            continue
        all_alpha[j] += 1

    if sum(all_alpha.values()) >= 26:
        return True

    return False


s = "leetcode"
print(checkIfPangram(s))