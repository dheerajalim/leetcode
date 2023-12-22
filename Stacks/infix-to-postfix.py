# precedence order
"""
1. ^
2. / and *
3. + and -
"""


def precedence_order(operator):
    if operator in ['+', '-']:
        return 1

    if operator in ['*', '/']:
        return 2

    if operator in ['^']:
        return 3

    return 0


def is_operator(item):
    if item in ['^', '/', '*', '+', '-']:
        return True

    return False


def infix_to_postfix(expression):
    if len(expression) == 0:
        return None

    stack = []
    postfix = []

    for char in expression:
        # If the character is an operand, add it to the postfix expression
        if char.isalnum():
            postfix.append(char)

        elif is_operator(char):
            # If the character is an operator, pop operators
            # from the stack and add them to the postfix
            # expression until the stack is empty or the top operator has lower precedence
            while stack and precedence_order(stack[-1]) >= precedence_order(char):
                postfix.append(stack.pop())
            stack.append(char)

        elif char == '(':
            # If the character is an open parenthesis, push it onto the stack
            stack.append(char)

        elif char == ')':
            # If the character is a close parenthesis, pop operators from the stack and add them to the
            # postfix expression until an open parenthesis is encountered
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())

            stack.pop()
    # Pop any remaining operators from the stack and add them to the postfix expression
    while stack:
        postfix.append(stack.pop())
    # Convert the postfix list to a string
    return "".join(postfix)

infix_expression = "a+b*(c^d-e)^(f+g*h)-i"
postfix_expression = infix_to_postfix(infix_expression)
print("Infix Expression:", infix_expression)
print("Postfix Expression:", postfix_expression)
