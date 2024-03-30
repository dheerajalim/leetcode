from binary_tree import *


def inorder_predecessor(root, val):
    if root is None:
        return None
    # to store predecessor
    predecessor = None

    curr = root
    # iterate until curr is None
    while curr:
        # if the val is greater than curr, hence curr is
        # a possible predecessor, hence move right to
        # find closer predecessor to val
        if val > curr.data:
            predecessor = curr.data
            curr = curr.right
        # if the val <= node, then move to left
        # to find a closer predecessor candidate
        # which is smaller than node
        else: # val <= root.data
            curr = curr.left

    return predecessor


root = inserttree()
val = 8
print(inorder_predecessor(root, val))
