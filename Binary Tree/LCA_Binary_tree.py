from binary_tree import *


def lca_binary_tree(root, n1, n2):
    if root is None:
        return None
    # in case if either n1 or n2 is found, we return that
    # as this can be the potential ancestor itself
    if root.data == n1 or root.data == n2:
        return root.data

    # we call the left and right subtree recursively
    lca_left = lca_binary_tree(root.left, n1, n2)
    lca_right = lca_binary_tree(root.right, n1, n2)

    # if both left and right return non None value
    # that means the node we are standing is the ancestor
    if lca_left and lca_right:
        return root.data

    # else we return the non None value from either
    # left or right, which ever hold non None value
    # this is possible in case bot the n1 and n2 are on same side
    return lca_left if lca_left else lca_right


root = inserttree()
n1 = 70
n2 = 80
print(lca_binary_tree(root, n1, n2))
