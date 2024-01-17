from binary_tree import *


# can be solved using the preorder traversal

def traversal(root, level, visible):
    if root is None:
        return
    # if at any point the number of items in left view list is equal to the level,
    # we add the node to the visible list
    if level == len(visible):
        visible.append(root.data)
    # traverse the left side first
    traversal(root.left, level + 1, visible)
    # after the left side traversal is over, move to right side
    traversal(root.right, level + 1, visible)


def left_view(root):
    visible = []

    traversal(root, 0, visible)

    return visible


root = inserttree()
print(left_view(root))
