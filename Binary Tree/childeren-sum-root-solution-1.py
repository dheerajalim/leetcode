from binary_tree import *

from collections import deque


# using Level Order Traversal
def children_sum_levelorder(root):
    if root is None:
        return 1

    dq = deque()

    dq.append(root)

    while dq:

        current_node = dq.popleft()
        # if the node exists add it to queue
        if current_node.left:
            dq.append(current_node.left)
        # if not then add a new node with 0 data
        else:
            dq.append(BinaryTree(0))

        if current_node.right:
            dq.append(current_node.right)
        else:
            dq.append(BinaryTree(0))
        # if both the last nodes are 0, then that means
        # the current node is leaf node, hence no action
        if dq[-1].data == 0 and dq[-2].data == 0:
            dq.pop()
            dq.pop()
            continue
        # if the sum of left and right node != root node
        # return False
        if dq[-1].data + dq[-2].data != current_node.data:
            return 0
        # if the right node we added was a leaf node, then
        # remove it to mantain the queue
        if dq[-1].data == 0:
            dq.pop()
        # if the left node we added was the leaf node
        # then remove the last node after swap to maintain queue
        elif dq[-2].data == 0:
            dq[-1], dq[-2] = dq[-2], dq[-1]
            dq.pop()

    return 1


#
# root = inserttree()
# print(children_sum_levelorder(root))


def check_children_sum_postorder(root):
    if root is None:
        return 0

    left_node = check_children_sum_postorder(root.left)
    if left_node == -1:
        return -1

    right_node = check_children_sum_postorder(root.right)
    if right_node == -1:
        return -1

    if left_node == 0 and right_node == 0:
        return root.data
    if (left_node == 0 and right_node != root.data) or (right_node == 0 and left_node != root.data):
        return -1

    if left_node + right_node != root.data:
        return -1

    return root.data


def children_sum_postorder(root):
    if check_children_sum_postorder(root) == -1:
        return False

    return True


# root = inserttree()
root = BinaryTree(11)
root.left = BinaryTree(1)
root.right = BinaryTree(10)
print(children_sum_postorder(root))
