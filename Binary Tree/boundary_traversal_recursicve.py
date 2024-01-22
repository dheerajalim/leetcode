from binary_tree import *


def left_boundary(root, stack):
    if root is None:
        return None

    if root.left is None and root.right is None:
        return root

    stack.append(root.data)

    left_b = left_boundary(root.left, stack)
    if left_b is None:
        left_boundary(root.right, stack)


def leaf_nodes(root, stack):
    if root is None:
        return

    if root.left is None and root.right is None:
        stack.append(root.data)

    leaf_nodes(root.left, stack)
    leaf_nodes(root.right, stack)


def right_boundary(root, right_stack):
    if root is None:
        return None

    if root.left is None and root.right is None:
        return root

    right_stack.append(root.data)

    right_b = right_boundary(root.right, right_stack)
    if right_b is None:
        right_boundary(root.left, right_stack)


root = inserttree()
root_left = root.left
root_right = root.right
stack = [root.data]
right_stack = []
left_boundary(root_left, stack)
print(stack)
leaf_nodes(root, stack)
print(stack)
right_boundary(root_right, right_stack)
stack.extend(right_stack[::-1])
print(stack)
