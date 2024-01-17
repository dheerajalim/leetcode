from binary_tree import *

from collections import deque


def traversal(root):
    if root is None:
        return

    dq = deque()
    dq.append((root, 0))
    hash_map = {}
    while dq:

        current_node = dq.popleft()
        # for each node we maintain (root, its position)
        node, node_pos = current_node[0], current_node[1]
        # hash map will have key as positon and value as the node data
        if hash_map.get(node_pos):
            hash_map[node_pos].append(node.data)
        else:
            hash_map[node_pos] = [node.data]
        # if left node exists we add it to queue
        # the position is on the left, hence current_node_pos -1
        if node.left:
            dq.append((node.left, node_pos - 1))
        # if right node exists we add it to queue
        # the position is on the right, hence current_node_pos -1
        if node.right:
            dq.append((node.right, node_pos + 1))

    return hash_map


def vertical_traversal(root):
    result = []
    # sort the hash map to get index in form
    # -2 , -1 , 0 , 1 , 2
    # get all the values of the hash map and append it to new list
    for item in sorted(traversal(root).items()):
        result.append(item[1])

    return result


root = inserttree()
print(vertical_traversal(root))
