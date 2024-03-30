from binary_tree import *


def is_identical(root1, root2):
    # if both the trees are empty then, identical
    if root1 is None and root2 is None:
        return True

    # if any one tree is emty , then not identical
    if root1 is None or root2 is None:
        return False

    # condition to check if the current node is same
    # and keep on traversing to left and right subtree recursively
    return root1.data == root2.data and is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)


root1, root2 = inserttree(), inserttree()

print(is_identical(root1, root2))
