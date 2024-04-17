"""
https://leetcode.com/problems/smallest-string-starting-from-leaf/description/?envType=daily-question&envId=2024-04-17
"""

from binary_tree import *


def tree_path(root, path_string, smallest_path):
    if root is None:
        return

    # if the node is leaf node, then we do the processing
    if root.left is None and root.right is None:
        # add the leaf node to the path
        path_string = chr(int(root.data) + 97) + path_string

        string_path = path_string
        # if the smallest_path contains a value, the compare
        # with the current path and update with min value
        if smallest_path:
            smallest_path[0] = min(smallest_path[0], string_path)
        # else just add the current path vale
        else:
            smallest_path.append(string_path)

    # while traversing keep on adding to the path
    # node that we add path_string after the new item as we need to store the path in
    # left to root and not root to leaf, so all new node in path is added before the previous node
    path_string = chr(int(root.data) + 97) + path_string

    # recursively call the left and right path
    tree_path(root.left, path_string, smallest_path)
    tree_path(root.right, path_string, smallest_path)


def smallest_from_leaf(root):
    # to store the smallest path
    smallest_path = []
    # to store the current path from root to leaf
    path_string = ""
    tree_path(root, path_string, smallest_path)

    return smallest_path[0]


root = inserttree()
printtree(root)

print(smallest_from_leaf(root))
