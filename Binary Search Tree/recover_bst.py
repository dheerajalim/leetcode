from binary_tree import *


def recover(root, prev, first, last):
    # follow the inorder traversal algo
    if root is None:
        return None

    # calling the left subtree recursively
    recover(root.left, prev, first, last)

    # if the previous node is present
    if prev[0]:
        # if the prev is greater than current node
        # and the first violator is None
        # then update the first violator to prev
        # last violator to curr
        if prev[0].data > root.data and first[0] is None:
            first[0] = prev[0]
            last[0] = root
        # else in case first violator is available
        # just update the last violator
        elif prev[0].data > root.data:
            last[0] = root

    # keep on moving the prev to current node in
    prev[0] = root

    # call the right subtree recursively
    recover(root.right, prev, first, last)


def recover_bst(root):
    # to store the previous node with
    # which we compare the current node
    prev = [None]
    # to keep the firs tand last element
    # that we will swap
    first, last = [None], [None]

    recover(root, prev, first, last)

    # swapping the forst and last violator
    if first[0] and last[0]:
        first[0].data, last[0].data = last[0].data, first[0].data


root = inserttree()
printtree(root)
recover_bst(root)
print('---')
printtree(root)
