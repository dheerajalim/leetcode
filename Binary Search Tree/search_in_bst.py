from binary_tree import *


def search_bst_recursive(root, key):
    # base case where the root is None
    # return False
    if root is None:
        return False

    # if the key matches with node, then return true
    if root.data == key:
        return True
    # move to the left if the key is smaller than root
    if root.data > key:
        # if we find true or false, just return
        return search_bst_recursive(root.left, key)
    # move to right if key is greater than root
    if root.data < key:
        return search_bst_recursive(root.right, key)


def search_bst_iteartive(root, key):
    # base case for a None root
    if root is None:
        return False

    curr = root
    # iterate until the curr node is not None
    # a None is basically returned by leaf node
    # this means we reached the end of BST but key not found
    while curr:

        # return true if key matches crr
        if curr.data == key:
            return True

        # else move to left or right side based on key
        # if greater than root, move right
        # else move left
        if curr.data > key:
            curr = curr.left

        elif curr.data < key:
            curr = curr.right

    return False


root = inserttree()
key = 2
print(search_bst_recursive(root, key))
print(search_bst_iteartive(root, key))
