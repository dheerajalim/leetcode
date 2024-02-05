"""
Given the root of a binary search tree, return a balanced binary search tree with the same node values.
If there is more than one answer, return any of them.
A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
"""

from binary_tree import *


def inorder_traversal(root, inorder_arr):
    if root is None:
        return None

    inorder_traversal(root.left, inorder_arr)
    inorder_arr.append(root)
    inorder_traversal(root.right, inorder_arr)


def balance_bst(root):
    arr = []
    # perform the inorder traversal
    # store the result in an array
    inorder_traversal(root, arr)
    start, end = 0, len(arr) - 1

    def create_bst(start, end, arr):
        # traverse through the array
        # if the start index > end index
        # the tree is traversed
        if start > end:
            return None

        # find the mid of inorder traversal
        # this will be the root
        middle = (start + end) // 2
        # create the root from the mid element
        root = BinaryTree(arr[middle].data)

        # recursively create the left subtree
        # by calling the left part from middle of the array
        root.left = create_bst(start, middle - 1, arr)
        # recursively create the right subtree
        # by calling the right part from middle of the array
        root.right = create_bst(middle + 1, end, arr)

        # return new root
        return root

    return create_bst(start, end, arr)




root = inserttree()
# printtree(root)
new_root = balance_bst(root)

printtree(new_root)
