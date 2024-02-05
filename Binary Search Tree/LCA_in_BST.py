from binary_tree import *


def find_lca(root, n1, n2):
    if root is None:
        return None

    # if both n1 and n2 are greater than root,
    # we know they will be on right
    # hence move right side
    if root.data < n1 and root.data < n2:
        return find_lca(root.right, n1, n2)

    # if both n1 and n2 are smaller than root
    # we will move to the left
    elif root.data > n1 and root.data > n2:
        return find_lca(root.left, n1, n2)

    # else if the
    # n1 is smaller than root and n2 is greater or vice versa,
    # then root is the LCA
    # also if n1 == root or n2 == root, then root will be LCA
    # Line 1:
    elif (root.data > n1 and root.data < n2) or (root.data < n1 and root.data > n2):
        return root.data
    # Line 2:
    elif root.data == n1 or root.data == n2:
        return root.data

    """ we can also skip the conditions in line 1 and line 2 and just return root
        as this will handle both line 1 and line 2 cases
    """
    # return root.data


root = inserttree()

print(find_lca(root, 1, 2))
