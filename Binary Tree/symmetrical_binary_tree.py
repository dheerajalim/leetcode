# check if the BT is Symmetric

from binary_tree import *


def check_symmetrical(root1, root2):
    # to check if  any of the root is None
    # then in that case if both are None we get True, else False
    # we use this condition as we can't do root.data for None root
    if root1 is None or root2 is None:
        return root1 == root2

    # we check the value of the root, if not equal return False
    if root1.data != root2.data:
        return False

    # move in the Preorder Traversal
    # for the root 1 : Root Left Right
    # for the root2 which would be mirror image
    # for reverse Preorder
    # for the root 2 : Root Right Left
    x = check_symmetrical(root1.left, root2.right)
    y = check_symmetrical(root1.right, root2.left)

    # we than return the end of left subtree and right subtree
    return x and y


def is_symmetrical(root):
    if root is None:
        return True

    root1 = root.left
    root2 = root.right

    return check_symmetrical(root1, root2)


root = inserttree()

print(is_symmetrical(root))
