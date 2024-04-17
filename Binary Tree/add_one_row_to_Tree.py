"""
https://leetcode.com/problems/add-one-row-to-tree/description/?envType=daily-question&envId=2024-04-16
"""

from binary_tree import *


def add_row(root, val, depth):
    if root is None:
        return None
    if depth == 1:
        new_root = BinaryTree(val)
        new_root.left = root
        root = new_root
        return root

    if depth == 2:
        left = root.left
        right = root.right
        new_root_left = BinaryTree(val)
        new_root_left.left = left

        new_root_right = BinaryTree(val)
        new_root_right.right = right

        root.left, root.right = new_root_left, new_root_right
        return root

    add_row(root.left, val, depth-1)
    add_row(root.right, val, depth-1)


root = inserttree()
printtree(root)

val = 1
depth = 2
root = add_row(root, val, depth)
printtree(root)
