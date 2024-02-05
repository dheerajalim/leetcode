from binary_tree import *


def find_smallest(root, k, count):
    # follow the Inorder traversal process
    if root is None:
        return None

    # we call the left subtree
    # if the left subtree returns Non None value,
    # that means the kth smallest element is present
    # we directly return that
    left_subtree = find_smallest(root.left, k, count)
    if left_subtree is not None:
        return left_subtree
    # else we increment the count until it becomes equal to k
    # and return the root.data
    count[0] += 1

    if count[0] == k:
        return root.data

    # search on the right part as well
    # note that we use return here as well, if we find it
    # or not on the right side
    # we directly return it, if found return the root data
    # else returns None
    return find_smallest(root.right, k, count)


def kth_smallest(root, k):
    count = [0]
    smallest_element = find_smallest(root, k, count)
    print(smallest_element)


root = inserttree()
k = 3
print(kth_smallest(root, k))
