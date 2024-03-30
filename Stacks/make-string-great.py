# https://leetcode.com/problems/make-the-string-great/

def makeGood(string):
    # empty string is also a good string
    if not string:
        return string
    stack = []
    # iterating through the characters
    for i in string:
        # if the current item and the top od stack have opposite
        # cases, then there difference is 32
        # we remove that element from stack
        if stack and abs(ord(stack[-1]) - ord(i)) == 32:
            stack.pop()
        # otherwise add the element to stack
        else:
            stack.append(i)
    # convert stack to string
    return "".join(stack)


input_string = "leEeetcode"
input_string = "abBAcC"
input_string = "s"
print(makeGood(input_string))
