# the node. right should work as node.next and left to None
from binary_tree import *


def flatten_binary_tree(root, prev):
    if root is None:
        return None

    flatten_binary_tree(root.right, prev)
    flatten_binary_tree(root.left, prev)

    root.right = prev[0]
    root.left = None

    prev[0] = root


root = inserttree()

flatten_binary_tree(root, [None])

curr = root
while curr:
    print(curr.data)
    curr = curr.right
