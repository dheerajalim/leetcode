"""
A complete binary tree is a binary tree whose:

All levels except the last one are completely filled. The last level may or may not be completely filled.
Nodes in the last level are as filled from left to right
"""

from binary_tree import *


# for a complete BT with lh == rh , the total nodes are 2^h -1 (h = height)
# where n is the left/right height
def number_of_nodes(root):
    if root is None:
        return 0

    lh, rh = 0, 0
    # navigating to the extreme left
    # to get the left height
    current = root
    while current:
        current = current.left
        lh += 1
    # navigating to extreme right
    # to get the right height
    current = root
    while current:
        current = current.right
        rh += 1
    # if lh == rh, then it is CBT
    # we use the formula 2^h - 1
    if lh == rh:
        return (2 ** lh) - 1

    # else, we follow the standard algo of 1 + lh + rh
    # for nodes whose lh != rh
    lh = number_of_nodes(root.left)
    rh = number_of_nodes(root.right)

    return 1 + lh + rh


root = inserttree()
print(number_of_nodes(root))
