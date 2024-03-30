from binary_tree import *


def max_node(root):
    if root is None:
        return float("-inf")

    left_max = max_node(root.left)
    right_max = max_node(root.right)

    return max(left_max, right_max, root.data)


root = inserttree()
print(max_node(root))
