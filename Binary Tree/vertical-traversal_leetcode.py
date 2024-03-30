# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/

from binary_tree import *

from collections import deque


def traversal(root):
    if root is None:
        return

    dq = deque()
    # for root, default is (root, index 0, level 0)
    dq.append((root, 0, 0))
    hash_map = {}
    while dq:

        current_node = dq.popleft()
        # for each node we maintain (root, its position, its level)
        node, node_pos, level = current_node[0], current_node[1], current_node[2]

        # we follow the level order traversal concept
        # along with adding the index and its level in hash map
        # this stores in format { index : {level : [node.data]}
        if hash_map.get(node_pos):
            if hash_map[node_pos].get(level):
                hash_map[node_pos][level].append(node.data)
            else:
                hash_map[node_pos][level] = [node.data]
        else:
            hash_map[node_pos] = {level: [node.data]}

        # if left node exists add it to the queue
        # with each left node, the level increases
        if node.left:
            dq.append((node.left, node_pos - 1, level + 1))
        # if right node exists add it to queue
        # with each right node, the level increases
        if node.right:
            dq.append((node.right, node_pos + 1, level + 1))

    return hash_map


def vertical_traversal(root):
    # sorting the hash map based on the index ex -2, -1 , 0 , 1, 2
    traversed_vertical = sorted(traversal(root).items())
    final_result = []
    for item in traversed_vertical:
        temp_result = list()
        # the values is a dict of form  {level : [node.data]}
        for value in item[1].values():
            # if the node data is a list with multiple values
            # this means there are nodes on same level
            # hence we sort them
            if len(value) > 1:
                value = sorted(value)
            # to have a single list on one level
            temp_result.extend(value)
        # appending all level wise list to main result list
        final_result.append(temp_result)

    return final_result


root = inserttree()

print(vertical_traversal(root))
