from binary_tree import *


class Node:
    # node class to store details
    def __init__(self, min_node, max_node, size):
        # to store the min node on the right side
        self.min_node = min_node
        # to store the max size on the left side
        self.max_node = max_node
        self.size = size


def largets_bst(root):
    if root is None:
        # if the root is None, we make sure that the root is valid
        # by making the min node on right as the largest
        # by making the max node on left as the smallest
        # this way Left largets < root < Right Smallest works
        min_node = float('inf')
        max_node = float('-inf')
        size = 0
        return Node(min_node, max_node, size)

    # use postorder to call the left and the right side
    left = largets_bst(root.left)
    right = largets_bst(root.right)

    # check the condition largets < root < Right
    # if true, then we update the min and max
    # the min is used for right side and max for left side
    # don't get confused
    if left.max_node < root.data < right.min_node:
        min_node = min(root.data, left.min_node)
        max_node = max(root.data, right.max_node)
        size = left.size + right.size + 1

    # else, just make sure that the root will never satisfy the
    # largest < root < Right condiiton
    else:
        # make the right min to the smallest value
        # make the left max to largets value
        # hence  left.max_node < root.data < right.min_node
        # this will always fail
        min_node = float('-inf')
        max_node = float('inf')
        size = max(left.size, right.size)

    return Node(min_node, max_node, size)


root = inserttree()
node_details = largets_bst(root)
print(node_details.size)
