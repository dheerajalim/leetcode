"""
https://leetcode.com/problems/remove-outermost-parentheses/

1 <= s.length <= 105
s[i] is either '(' or ')'.
s is a valid parentheses string.


The idea is to keep a count of the open bracket and keep on incrmenting that
once we find the close bracket we decrement the count
If the count > 0 , then the bracket goes in the result
"""


def remove_outer_para(s : str):

    result  = ""
    open_bracket = 0

    for i in s:

        if i == ')':
            open_bracket -= 1

        if open_bracket > 0:
            result += i

        if i =='(':
            open_bracket += 1

    return result


s ="(()())(())"
# s = "(()())(())(()(()))"
print(remove_outer_para(s))


