def is_palindrome(string, start, end):
    check_string = string[start: end + 1]

    if check_string == check_string[::-1]:
        return True

    return False


def backtracking(string, idx, curr, result):
    # if we reach the end of string then we add it to the result
    if idx == len(string):
        result.append(curr.copy())

    # we iterate from the current idx towards the end of string
    for i in range(idx, len(string)):
        # if the current partition from idx to i is a palindrome
        # then we store that part from idx:i+1 to curr
        # and then check the next part which is i+1
        if is_palindrome(string, idx, i):
            curr.append(string[idx: i + 1])
            backtracking(string, i + 1, curr, result)
            # once the include part is completed, we pop and
            # start the exclude part as well
            curr.pop()


def partition(string):
    result = []
    curr = []

    backtracking(string, 0, curr, result)
    return result


s = "aab"
print(partition(s))
