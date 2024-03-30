from binary_tree import *


def height(root):
    if root is None:
        return 0
    # find the recursive height of left sub tree
    left_height = height(root.left)
    # find the recursive height if right sub tree
    right_height = height(root.right)

    # add 1 to include the root from whose left and right
    # recursive calls were made
    return max(left_height, right_height) + 1


root = inserttree()

print(height(root))
