from binary_tree import *


def ceiling_bst(root, key):
    ceiling = None

    if root is None:
        return None

    curr = root

    while curr:
        # if we find exact match, then return that
        if curr.data == key:
            return curr.data
        # if the root data is greater than key
        # this means this is potential ceil,
        # hence update ceiling value and move left
        # to find the more closer/smaller ceil value
        if curr.data > key:
            ceiling = curr.data
            curr = curr.left
        # else keep searching on the right side
        elif curr.data < key:
            curr = curr.right

    return ceiling


root = inserttree()
print(ceiling_bst(root, 40))
