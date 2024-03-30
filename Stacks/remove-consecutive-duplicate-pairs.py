def remove_consecutive_duplicate_pairs(input_str):
    if input_str is None or input_str == "":
        return input_str

    stack = []  # Create an empty stack

    # iterate through the items of the input
    for i in input_str:
        # for case where the stack is empty but the input string has data
        if not stack:
            stack.append(i)
        # if the last item in stack is equal to the input item, the pop the item
        # this is a pair
        elif stack[-1] == i:
            stack.pop()
        # if not a pair, the just append
        else:
            stack.append(i)
    # return string
    return "".join(stack)


input_str = "aaabbaaccd"
input_str = "aaa"
print(remove_consecutive_duplicate_pairs(input_str))
