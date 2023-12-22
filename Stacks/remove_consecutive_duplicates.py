def remove_consecutive_duplicates(input_str):
    if input_str is None or "":
        return input_str

    stack = []  # create a stack

    for i in input_str:
        # edge case for the empty stack where the
        # items are still present in input
        if not stack:
            stack.append(i)
        # if the top of stack and input (i) are not equal , append it to stack
        if i != stack[-1]:
            stack.append(i)
    # convert list to string
    return "".join(stack)


input_str = "aaaaaabaabccccccc"

print(remove_consecutive_duplicates(input_str))
