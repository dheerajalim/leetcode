# print the level order traversal, where each level is
# is printed in new line

from binary_tree import *

from collections import deque


def level_order_line(root):
    if root is None:
        return None

    dq = deque()
    # add root to queue
    dq.append(root)
    # the addition of None is to understand the line change
    dq.append(None)

    while len(dq) > 1:

        curr_node = dq.popleft()
        # if this condition is true, means the line needs to be changed
        # we add a None and a new line is printed, to demo new line
        if curr_node is None:
            dq.append(None)
            print()
            continue
        # else print the current node
        print(curr_node.data, end=" ")
        if curr_node.left:
            dq.append(curr_node.left)

        if curr_node.right:
            dq.append(curr_node.right)


root = inserttree()
level_order_line(root)
