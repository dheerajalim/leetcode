from binary_tree import *


# if leaf node, delete it
# if no right, replace with right node, or viceversa
# if both left and right available, find the inorder successor
# > always taking the next upper node


# function to find the inorder successor
# keep on moving to left to get the leaf node
# that is the successor node
def inorder_successor(node):
    while node.left:
        node = node.left

    return node.data


def delete_from_bt(root, key):
    if root is None:
        return None

    # BST algo for key if greater than root > move right
    # else move left
    if root.data > key:
        root.left = delete_from_bt(root.left, key)

    elif root.data < key:
        root.right = delete_from_bt(root.right, key)

    # if the key == root.data, this is to be deleted
    else:
        # if the key right node is none, we return left node
        if root.right is None:
            return root.left
        # if the left node is node, we return right node
        # these above two conditons also handle the leaf nodes
        # as any ways for a leaf node, left or right will also return None
        elif root.left is None:
            return root.right
        # if the root matches but has bot the left and right node
        else:
            # find the inorder successor, by moving to rightmost node
            # then going extreme left of it towards leaf node
            # this is the next upper value
            successor_key = inorder_successor(root.right)
            # replace the roots value with this next upper value
            root.data = successor_key
            # delete this next upper node recursively
            # pass this root.right as the new root and , next upper value
            # as the key. The return value is update in the roots right
            root.right = delete_from_bt(root.right, successor_key)

    # return the root
    return root


root = inserttree()
key = 10
new_root = delete_from_bt(root, key)

printtree(new_root)
