from binary_tree import *


def insert_bst(root, key):

    # if the root is None, we create a new Node
    # since the new node is always inserted on the leaf
    # based on the way BST works
    if root is None:
        return BinaryTree(key)

    # call for left subtree, if the key is smaller than root
    # and then we assign the return value to root.left as the new value
    # would technically be the left node of root
    if root.data > key:
        root.left = insert_bst(root.left, key)

    # call for right subtree, if the key is greater than root
    # and then we assign the return value to root.right as the new value
    # would technically be the right node of root
    elif root.data < key:
        root.right = insert_bst(root.right, key)

    # then just return the root, so that every parent node
    # will get its child to which it was connected
    # this is useful when already existing node is given as key
    # in that case root.data > key and root.data < key
    # are ignore and we directly return root
    return root

root = inserttree()
key = 20
new_root = insert_bst(root, key)

printtree(new_root)
