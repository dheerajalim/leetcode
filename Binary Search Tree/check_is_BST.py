from binary_tree import *


def check(root, min_val, max_val):
    # base case if the root is None, it returns True
    if root is None:
        return True

    # check if the left subtree is also a BST
    # for each node, the min value will be the existing min,
    # but max will update based on the root data
    left_part = check(root.left, min_val, root.data)
    # check if the right subtree is a BST
    # for each node, the max value will be existing max,
    # but the min will update based on the root data
    right_part = check(root.right, root.data, max_val)

    # check if the left part is true/false, right part is true/false
    # and the node is in range of min and max values
    return left_part and right_part and (min_val < root.data < max_val)


def check_BST(root):
    # initial values for min max that will be applicable for root of BT
    min_value, max_value = float('-inf'), float('inf')
    return check(root, min_value, max_value)


root = inserttree()

print(check_BST(root))
