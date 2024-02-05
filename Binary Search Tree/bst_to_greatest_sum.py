"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is
changed to the original key plus the sum of all keys greater than the original key in BST.
"""

from binary_tree import *


# the idea is to follow reverse inorder : Right Root Left


def bst_to_greatest_sum(root):
    # to maintain the previous pointer
    prev = [0]

    def calculate(root, prev):
        # the base case of inorder traversal
        if root is None:
            return None

        # recursively call the right side
        calculate(root.right, prev)

        # the root data is updated to its' data
        # and the prev pointer data
        root.data = prev[0] + root.data
        # update the prev to the current root.data
        prev[0] = root.data

        # recursively call the left side
        calculate(root.left, prev)

    calculate(root, prev)

    # return the root of the update tree
    return root


root = inserttree()
bst_to_greatest_sum(root)
printtree(root)
