"""
https://leetcode.com/problems/delete-leaves-with-a-given-value/description/?envType=daily-question&envId=2024-05-17
"""

from binary_tree import *


def remove_leaf_nodes(root, target):
    # if the root is None return None
    if root is None:
        return None

    # the case where we need to remove the leaf node if it matches target
    if root.left is None and root.right is None:
        if root.data == target:
            return None
        # else we return the node as it is
        return root

    # update the left and right value of the node in recursion
    root.left = remove_leaf_nodes(root.left, target)

    root.right = remove_leaf_nodes(root.right, target)

    # this is again checked so that if a node is now a leaf, it is deleted
    if root.left is None and root.right is None:
        if root.data == target:
            return None
        return root

    return root


root = inserttree()
target = 2
printtree(root)
print("+++++")
new_root = remove_leaf_nodes(root, target)

printtree(new_root)
