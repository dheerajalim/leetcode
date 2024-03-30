from binary_tree import *

from collections import deque


def bottom_view(root):
    if root is None:
        return

    dq = deque()
    dq.append((root, 0))
    hash_map = {}

    while dq:

        current_node = dq.popleft()
        # for each node we maintain (root, its position)
        node, node_pos = current_node[0], current_node[1]
        # hash map will have key as position and value as the node data
        # for every new position, it will replace the existing position data
        hash_map[node_pos] = node.data
        # if left node exists we add it to queue
        # the position is on the left, hence current_node_pos -1
        if node.left:
            dq.append((node.left, node_pos - 1))
        # if right node exists we add it to queue
        # the position is on the right, hence current_node_pos -1
        if node.right:
            dq.append((node.right, node_pos + 1))

    result = []
    for item in sorted(hash_map):
        result.append(hash_map[item])
    return result


root = inserttree()
print(bottom_view(root))
