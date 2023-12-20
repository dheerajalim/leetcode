# given an input string , check for balanced parenthesis

# Possible parenthesis : () , {}, []

def check_parenthesis(input_str):
    stack_list = list() # creates a stack DS
    # check for an invalid string or just one element
    if input_str is None or len(input_str) == 1:
        return False
    # An empty string is anyways balanced
    if len(input_str) == 0:
        return True

    # iterating through all the items
    for item in input_str:
        # adding the open brackets to the stack
        if item in ['(', '{', '[']:
            stack_list.append(item)
        # if the very first item in string is closing bracket, then this is not balanced
        elif len(stack_list) == 0:
            return False
        # we take the last available item from the lsit/stack and compare
        # if there is a valid closing bracket, then continue else return False
        elif item in [')', '}', ']']:
            last_stack_item = stack_list.pop()
            if (last_stack_item == '(' and item == ')') or (last_stack_item == '{' and item == '}') or (
                    last_stack_item == '[' and item == ']'):
                continue
            else:
                return False
    # after the iteration ends, if we still have a non empty stack, then this is not balanced
    if stack_list:
        return False
    return True


input_str = "((())"

print(check_parenthesis(input_str))
