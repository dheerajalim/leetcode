from binary_tree import *

from collections import deque

def even_odd(root):

    if root is None:
        return None

    level = 0
    dq = deque()

    dq.append([root, level])

    while dq:
        size = len(dq)
        nodes_at_level_even = float('-inf')
        nodes_at_level_odd = float('inf')
        for _ in range(size):
            current_node, level = dq.popleft()

            if level % 2 == 0:

                if current_node.data % 2 != 1:
                    return False

                if current_node.data > nodes_at_level_even:
                    nodes_at_level_even = current_node.data
                else:
                    return False

            if level % 2 == 1:
                if current_node.data % 2 != 0:
                    return False

                if current_node.data < nodes_at_level_odd:
                    nodes_at_level_odd = current_node.data
                else:
                    return False

            if current_node.left:

                dq.append([current_node.left, level+1])

            if current_node.right:

                dq.append([current_node.right, level+1])

    return True


root = inserttree()

print(even_odd(root))