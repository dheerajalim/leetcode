# Improved Solution

from binary_tree import *


def children_sum(root):
    # base condition
    if root is None:
        return 0

    # condition for the leaf nodes, if we are at leaf node
    # then simply return the root's data
    if root.left is None and root.right is None:
        return root.data

    # recursively call the left subtree
    left_children = children_sum(root.left)
    # in case left subtree has invalid child sum, we stop
    if left_children == float('-inf'):
        return float('-inf')
    # recursively call the right subtree
    right_children = children_sum(root.right)
    # in case right subtree has invalid child sum, we stop
    if right_children == float('-inf'):
        return float('-inf')

    # condition to check the child sum property
    # if left node and right node sum = root node data
    # and the left subtree and right subtree is not float('-inf')
    # then this is valid
    if left_children != float('-inf') and right_children != float('-inf') and (root.data == left_children + right_children):
        # for a valid case return the root.data
        return root.data
    # else return float('-inf') to mark invalid
    return float('-inf')


def check_children_sum(root):
    if children_sum(root) == float('-inf'):
        return False
    return True


root = inserttree()
print(check_children_sum(root))
