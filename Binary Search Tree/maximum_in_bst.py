from binary_tree import *


def maximum_in_bst(root):
    # if the tree is empty
    # can return None, depends on question
    if root is None:
        return -1

    # if the root right subtree is not there
    # then root is itself the maximum
    if root.right is None:
        return root.data

    # else go to the rightmost node
    # that node is the maximum
    else:
        curr = root
        while curr.right:
            curr = curr.right

        return curr.data


root = inserttree()
print(maximum_in_bst(root))
