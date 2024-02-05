"""
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree
is now the root of the tree, and every node has no left child and only one right child.

https://leetcode.com/problems/increasing-order-search-tree/description/
"""

from binary_tree import *


def bst_to_linked_list(root):
    prev = [None]
    new_root = [None]

    def convert(root, prev, new_root):
        if root is None:
            return None

        # inorder traversal, for left subtree
        convert(root.left, prev, new_root)

        # if the prev is none, the root will be the head of
        # linked list
        if prev[0] is None:
            new_root[0] = root

        # otherwise update the prev.right to root
        # root.left to None
        else:
            prev[0].right = root
            root.left = None

        # keep on moving the prev to the current root
        prev[0] = root

        convert(root.right, prev, new_root)

    convert(root, prev, new_root)

    return new_root[0]


root = inserttree()

new_root = bst_to_linked_list(root)

printtree(new_root)
