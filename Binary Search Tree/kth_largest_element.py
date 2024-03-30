from binary_tree import *


def find_largest(root, k, count):
    # follow the Reverse Inorder traversal process
    # as we need to find the largest, we need to traverse
    # right side first : Right Root Left
    if root is None:
        return None

    # we call the right subtree
    # if the right subtree returns Non None value,
    # that means the kth the largest element is present
    # we directly return that
    right_subtree = find_largest(root.right, k, count)
    if right_subtree is not None:
        return right_subtree
    # else we increment the count until it becomes equal to k
    # and return the root.data
    count[0] += 1

    if count[0] == k:
        return root.data

    # search on the left part as well
    # note that we use return here as well, if we find it
    # or not on the left side
    # we directly return it, if found return the root data
    # else returns None
    return find_largest(root.left, k, count)


def kth_largest(root, k):
    count = [0]
    largest_element = find_largest(root, k, count)
    print(largest_element)


root = inserttree()
k = 3
kth_largest(root, k)
