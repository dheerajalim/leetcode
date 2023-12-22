# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/

def minLength(string):
    # using stack DS to understand if the pair AB or CD is present
    stack = []  # to push the items into this stack

    for char in string:
        # if the stack is not empty and last element is A or C and the current char is B or D
        # then we remove the last element from stack
        if stack and ((char == 'B' and stack[-1] == 'A') or (char == 'D' and stack[-1] == 'C')):
            stack.pop()
        # Otherwise keep on appending the char
        else:
            stack.append(char)
    # the char inside the stack is the min length of new string
    return len(stack)


input_str = "ABFCACDB"

print(minLength(input_str))
