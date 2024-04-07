"""
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/?envType=daily-question&envId=2024-04-04

The idea here is to get the maximum number of open brackets
whenever a open bracket is encountered, we increment the count
whenever the closing bracket is encountered, we take the max value of the open brackets first
and then we decrement the count. This way we have the max_count containing the maximum
number fo open "(" brackets
"""


def max_depth(string):
    # to store the max count
    max_count = 0
    # to store the current count of the parenthesis
    count = 0
    # iterate through the string
    for s in string:
        # if the bracket is ( then we increment the count
        if s == "(":
            count += 1
        # if the bracket is ), then we decrement the count
        # and also we will keep on storing the max count of
        # open brackets as this is what we need the max
        elif s == ")":
            max_count = max(max_count, count)
            count -= 1

    # return the max count
    return max_count


string = "(1+(2*3)+((8)/4))+1"

print(max_depth(string))
