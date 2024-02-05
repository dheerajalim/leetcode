from binary_tree import *


def minimum_in_bst(root):
    # if the tree is empty
    # can return None, depends on question
    if root is None:
        return -1

    # if the root left subtree is not there
    # then root is itself the minimum
    if root.left is None:
        return root.data

    # else go to the leftmost node
    # that node is the minimum
    else:
        curr = root
        while curr.left:
            curr = curr.left

        return curr.data

root = inserttree()
print(minimum_in_bst(root))
