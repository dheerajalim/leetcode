# https://leetcode.com/problems/remove-k-digits/

"""
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
"""


# can be solved using NSE to left concept

def remove_k_digits(num, k):
    stack = []

    i = 0
    # edge case if the length of input and k is same then all
    # digits are removed
    if len(num) == k:
        return 0

    # looping to find the NSE on left
    while i < len(num):
        # poping the stack if the current element is less than top of stack
        # and also until k becomes 0 i.e k digits are removed
        while stack and k and num[i] < stack[-1]:
            stack.pop()
            k -= 1

        # once the stack has min element on top
        # append the current item to stack, note that if the stack
        # is empty and curr item is 0 , we ignore example 0132 is not valid
        # whereas 132 is valid
        if not stack and num[i] != '0':
            stack.append(num[i])
        # otherwise just append to the stack
        elif stack:
            stack.append(num[i])

        i += 1
    # to solve the edge case, where the number is increasing order
    # example : 12345, then the above code would not work
    # or in case not all k digits were removed
    # we just fetch then remove the last k digits
    if k:
        stack = stack[0:-k]

    return "".join(stack) if stack else "0"


num = "1432219"
num = "10200"
num = "10"
k = 2
print(remove_k_digits(num, k))
