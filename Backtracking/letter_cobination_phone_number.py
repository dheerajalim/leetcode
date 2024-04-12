def backtracking(digits, alpha, idx, curr, result):
    if len(curr) == len(digits):
        result.append("".join(curr.copy()))
        return

    # alpha is a list of each digits alphabet example 23 = [abc],[def]
    # we iterate through each item of alpha which is a list
    for i in range(idx, len(alpha)):

        # taking the length of current digit alpha equivalent
        curr_set = len(alpha[i])

        # iterating through each item of this alpha equivalent and
        # calling the backtracking template
        for x in range(curr_set):
            # adding the current item to the curr list
            curr.append(alpha[i][x])
            # calling the backtracking on the next list in alpha
            # basically we will always start with first index of each list
            backtracking(digits, alpha, i + 1, curr, result)

            curr.pop()


def letter_combinations(digits):
    if len(digits) == 0:
        return []
    result = []
    curr = []
    mapping = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
    alpha = []
    for i, num in enumerate(digits):
        alpha.append(mapping[int(num)])

    backtracking(digits, alpha, 0, curr, result)

    return result


digits = "23"
print(letter_combinations(digits))
