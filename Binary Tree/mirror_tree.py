from binary_tree import *


def mirror_tree(root):
    if root is None:
        return None
    # recursively call the left subtree
    mirror_tree(root.left)
    # recursively call the right subtree
    mirror_tree(root.right)
    # swap the nodes on the left and right side of the current root node
    root.left, root.right = root.right, root.left

    # return root to the parent node
    return root


root = inserttree()
new_root = mirror_tree(root)

printtree(new_root)
