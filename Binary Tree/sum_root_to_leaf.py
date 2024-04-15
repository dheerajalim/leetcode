"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=daily-question&envId=2024-04-15
"""

from binary_tree import *


def parse_digits(root, digits, result):
    # base case, if root is None
    if root is None:
        return

    # if the left and right is a None, then this is a leaf node
    # and we consider path fro root to leaf and add it to result array
    if root.left is None and root.right is None:
        digits += str(root.data)
        result[0] += int(digits)
        return

    # create the digits while traversing from root node to downwards
    digits += str(root.data)

    # call the left and right subtree recursively
    parse_digits(root.left, digits, result)
    parse_digits(root.right, digits, result)


def sum_digits(root):
    digits = ""
    result = [0]

    parse_digits(root, digits, result)

    # return the sum of result array
    return result[0]

root = inserttree()

printtree(root)

print(sum_digits(root))
