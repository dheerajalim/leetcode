from binary_tree import *


def node_at_distance_k(root, k):
    if root is None:
        return None

    if k == 0:
        # this indicates that the required level is reached
        print(root.data, end=" ")
        return
    # iterating on the left side with each level
    # going down and reducing k by 1
    node_at_distance_k(root.left, k - 1)
    # iterating on the right side with each level
    # going down and reducing k by 1
    node_at_distance_k(root.right, k - 1)


root = inserttree()
node_at_distance_k(root, 2)
