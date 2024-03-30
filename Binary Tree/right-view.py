from binary_tree import *


# solving using reverse Preorder traversal i.e. Root Right Left

def traverse(root, level, visible):
    if root is None:
        return
    # if at any point the number of items in right view list is equal to the level,
    # we add the node to the visible list
    if level == len(visible):
        visible.append(root.data)
    # traverse the right side first
    traverse(root.right, level + 1, visible)
    # after the right sice traversal is over, move to left side
    traverse(root.left, level + 1, visible)


def right_view(root):
    visible = []
    traverse(root, 0, visible)

    return visible


root = inserttree()
print(right_view(root))
