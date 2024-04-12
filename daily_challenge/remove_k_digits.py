def remove_k_digits(num, k):
    stack = []

    if len(num) == k:
        return "0"

    for i in range(len(num)):

        while stack and k and num[i] < stack[-1]:
            stack.pop()
            k -= 1

        if not stack and num[i] != '0':
            stack.append(num[i])

        elif stack:
            stack.append(num[i])

    if k > 0:
        stack = stack[:-k]

    return "".join(stack) if stack else "0"


num = "10"
k = 1

print(remove_k_digits(num, k))
