from binary_tree import *


def is_leaf(root):
    if root.left is None and root.right is None:
        return True

    return False


def left_boundary(root, boundary_nodes):
    curr = root.left

    while curr:
        if not is_leaf(curr):
            boundary_nodes.append(curr.data)
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right


def leaf_nodes(root, boundary_nodes):
    if root is None:
        return
    if is_leaf(root):
        boundary_nodes.append(root.data)

    leaf_nodes(root.left, boundary_nodes)
    leaf_nodes(root.right, boundary_nodes)


def right_boundary(root, boundary_nodes):
    curr = root.right
    temp_right_boundary_nodes = []
    while curr:
        if not is_leaf(curr):
            temp_right_boundary_nodes.append(curr.data)
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left

    boundary_nodes.extend(temp_right_boundary_nodes[::-1])


def boundary_traversal(root):
    if root is None:
        return []

    if is_leaf(root):
        return [root.data]

    boundary_nodes = [root.data]
    left_boundary(root, boundary_nodes)
    leaf_nodes(root, boundary_nodes)
    right_boundary(root, boundary_nodes)

    return boundary_nodes

root = inserttree()

print(boundary_traversal(root))