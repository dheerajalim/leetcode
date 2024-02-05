from binary_tree import *


def search_bst(root, key):
    if root is None:
        return False

    if root.data == key:
        return True
    if root.data > key:
        return search_bst(root.left, key)
    if root.data < key:
        return search_bst(root.right, key)



root = inserttree()
key = 40
print(search_bst(root, key))