"""
The idea is to balance out ) with ( bracket

We wil maintain two stacks : 1 for  the brackets and the other one for the *;
                             we store the index of these items in stack
Whenever the ) is received,
 we check if we have ( to balance
 else: we check if start is present to balance
 else: return Fasle since there is no one to balance ) and going ahead makes no sense


 Once we complete the iteration, we check if both the stacks are not empty
 we then iterate until any one is empty and we need to cancel all ( brackets with stars
 that appear after tge bracket as if a start appears before this bracket, then it makes no sense

 If the len of the bracket_stack is == 0 , then all a re balanced else it cannot be a balance parenthesis
"""


def valid_para(s):
    # convert the string to list
    str_lst = list(s)

    # to store the brackets and stack separately
    bracket_stack, star_stack = [], []

    for idx, item in enumerate(str_lst):

        if item == "(":
            bracket_stack.append(idx)

        elif item == ")":

            if bracket_stack:
                bracket_stack.pop()

            elif star_stack:
                star_stack.pop()

            else:
                return False

        elif item == "*":
            star_stack.append(idx)

    # we need to cancel all the "(" with "*", and "*" should come after (
    while bracket_stack and star_stack:
        # if  the star pos is after bracket position, then we cancel both
        # hence pop from both the stack
        if star_stack[-1] > bracket_stack[-1]:
            bracket_stack.pop()
            star_stack.pop()

        # if a bracket cannot be cancelled by the stack, we return False
        else:
            return False

    # check the len of the bracket stack
    return len(bracket_stack) == 0


s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"

print(valid_para(s))
