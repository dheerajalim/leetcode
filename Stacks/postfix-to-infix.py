def isOperator(value):
    if value in ('*', '/', "+", "-", "^", "(", ")"):
        return True

    return False


def postfix_to_infix(expression):
    stack = []

    for i in expression:
        # if this is an operand then push to stack
        if not isOperator(i):
            stack.append(i)

        else:
            # the last element is the second operator , hence we create op1 and op2
            op2 = stack.pop()
            op1 = stack.pop()
            str = "(" + op1 + i + op2 + ")"
            stack.append(str)

    return stack.pop()


str = "ab*c+"
str = "abc++"
print(postfix_to_infix(str))
