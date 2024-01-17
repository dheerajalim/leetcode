from binary_tree import *

from collections import *
def width_bt(root):

    if root is None:
        return

    dq = deque()
    dq.append((root,0))
    hash_map = {}

    while dq:

        current_node = dq.popleft()
        node, node_pos = current_node[0], current_node[1]

        if hash_map.get(node_pos):
            hash_map[node_pos] += 1
        else:
            hash_map[node_pos] = 1

        if node.left:
            dq.append((node.left, node_pos+1))

        if node.right:
            dq.append((node.right, node_pos+1))

    return max(hash_map.values())

root = inserttree()

print(width_bt(root))

