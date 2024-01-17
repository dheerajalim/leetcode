from binary_tree import *


def number_of_nodes(root):
    if root is None:
        return 0
    # find the nodes on the left
    lh = number_of_nodes(root.left)
    # find the nodes on the right
    rh = number_of_nodes(root.right)
    # return the left nodes count + right nodes count + 1 (root node)
    return lh + rh + 1


root = inserttree()

print(number_of_nodes(root))
