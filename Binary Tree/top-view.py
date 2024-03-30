from binary_tree import *

from collections import deque


def traverse(root):
    if root is None:
        return

    dq = deque()
    dq.append((root, 0))
    hash_map = dict()

    while dq:
        current_node = dq.popleft()
        node, node_pos = current_node[0], current_node[1]
        # if the hash map key exists, then do not do anything
        # else just add the key and its node value
        if not hash_map.get(node_pos):
            hash_map[node_pos] = node.data

        if node.left:
            dq.append((node.left, node_pos - 1))

        if node.right:
            dq.append((node.right, node_pos + 1))

    return hash_map


def top_view(root):
    result = []

    hash_map = traverse(root)
    for item in sorted(hash_map):
        result.append(hash_map[item])

    return result


root = inserttree()
print(top_view(root))
