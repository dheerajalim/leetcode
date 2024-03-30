from binary_tree import *


def generate_bst(preorder, pos, ub):
    # if the pos variable to check inside
    # preorder list is greater than preorder array size, then
    # return None
    if pos[0] >= len(preorder):
        return None

    # if the item in preorder list that will be made a node
    # is greater than the upper bound at that position
    # return None
    if preorder[pos[0]] > ub:
        return None

    # create root and update the position in preorder list
    root = BinaryTree(preorder[pos[0]])
    pos[0] += 1

    # the left subtree will have upper bound as it parent node value
    root.left = generate_bst(preorder, pos, root.data)
    # the right subtree node will have it's
    # upper bound same as its parent ub
    root.right = generate_bst(preorder, pos, ub)

    # finally return the root
    return root


def bst_from_preorder(preorder):
    pos = [0]
    # max value as the upper bound
    ub = float('inf')

    return generate_bst(preorder, pos, ub)


preorder = [8, 5, 1, 7, 10, 12]
root = bst_from_preorder(preorder)

printtree(root)
