def isOperator(value):
    if value in ('*', '/', "+", "-", "^", "(", ")"):
        return True

    return False


def prefix_to_infix(expression):
    stack = []
    i = len(expression) - 1

    while i >= 0:
        if not isOperator(expression[i]):
            stack.append(expression[i])
            i -= 1
        else:
            str = "(" + stack.pop() + expression[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1

    return stack.pop()


str = "*-A/BC-/AKL"
print(prefix_to_infix(str))
