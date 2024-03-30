from binary_tree import *

from collections import deque


def level_order_traversal(root):
    if root is None:
        return
    # creating the queue
    dq = deque()
    # appending the queue with the root
    dq.append(root)
    # iterating until the queue is not empty
    while dq:
        # pop the front of the queue and print it
        current_node = dq.popleft()
        print(current_node.data, end=" ")
        # if the left for the node exits
        # append it to the queue
        if current_node.left:
            dq.append(current_node.left)
        # if the right for the node exits
        # append it to the queue
        if current_node.right:
            dq.append(current_node.right)

        # Note: after each iteration we take the front of the queue


root = inserttree()
level_order_traversal(root)

# 10
# 20
# 40
# -1
# -1
# -1
# 30
# 50
# 70
# -1
# -1
# 80
# -1
# -1
# 60
# -1
# -1
