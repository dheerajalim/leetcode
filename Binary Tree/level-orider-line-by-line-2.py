from binary_tree import *

from collections import deque


def level_order(root):
    if root is None:
        return None

    dq = deque()

    dq.append(root)

    while dq:
        # get the size of the queue
        size = len(dq)
        # based on the size iterate the queue
        for i in range(size):
            current_node = dq.popleft()
            if current_node.left:
                dq.append(current_node.left)
            if current_node.right:
                dq.append(current_node.right)
            # print the front of queue
            # any element in the same iteration gets printed
            # in same line
            print(current_node.data, end=" ")
        # adds a print to new line
        print()


root = inserttree()
level_order(root)
