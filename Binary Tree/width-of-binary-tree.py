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


# easier solution
def width_bt_easier(root):
    if root is None:
        return None

    dq = deque()
    dq.append(root)

    max_width = 0
    while dq:
        # taking the current size of the dequeu
        size = len(dq)
        # comparing it with the previous max width
        # each level size will be qual to the size of dequeu at present
        max_width = max(max_width, size)

        for _ in range(size):

            current_node = dq.popleft()

            if current_node.left:
                dq.append(current_node.left)

            if current_node.right:
                dq.append(current_node.right)

    return max_width

root = inserttree()

print(width_bt(root))

