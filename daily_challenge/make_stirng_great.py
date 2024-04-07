def make_good(s: str) -> str:
    stack = [s[0]]
    n = len(s)

    for i in range(1, n):
        if stack and abs(ord(s[i]) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(s[i])

    return "".join(stack)
