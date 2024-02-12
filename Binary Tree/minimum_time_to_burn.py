from binary_tree import *

from collections import deque


def find_time(target, node_parent_map: dict):
    # store the already visited/burnt node
    visited = dict()
    dq = deque()
    # starting from the target node, hence add it to queue
    # similar to level order traversal
    dq.append(target)
    # the target node is already visited, hence update the
    # visited hash map
    visited[target] = 1
    # to store the time to burn the tree
    min_time = 0

    while dq:
        size = len(dq)
        # if this is set to 1, that means atleast one adjacent
        # node is burnt, and the time is taken
        burn_flag = 0
        # follow the level order line by line algo
        for i in range(size):
            current = dq.popleft()
            # if the left node exist and is not burnt already/visited
            if current.left and not visited.get(current.left):
                # add to queue, mark it visited and update the burn flag
                dq.append(current.left)
                visited[current.left] = 1
                burn_flag = 1

            if current.right and not visited.get(current.right):
                # add to queue, mark it visited and update the burn flag
                dq.append(current.right)
                visited[current.right] = 1
                burn_flag = 1
            # this condition is for the parent node
            # which is also a possibility for burning
            if node_parent_map.get(current) and not visited.get(node_parent_map[current]):
                dq.append(node_parent_map[current])
                visited[node_parent_map[current]] = 1
                burn_flag = 1
        # if the flag is set to 1, that means something is burnt
        # in a level, hence we increment time
        if burn_flag:
            min_time += 1
    # return the time taken to burn tree
    return min_time


def node_parent_relation(root, target: int):
    # following the level order traversal algo
    if root is None:
        return

    dq = deque()
    dq.append(root)
    # to store parent - node relation
    hash_map = dict()
    # to store the target node as the give value is integer
    target_node = None
    while dq:
        current = dq.popleft()
        # to check if the current node data is equal to
        # the target node
        if current.data == target:
            target_node = current
        # level order algo steps
        if current.left:
            dq.append(current.left)
            hash_map[current.left] = current

        if current.right:
            dq.append(current.right)
            hash_map[current.right] = current

    # return the parent-node relation hash map and the
    # target node
    return target_node, hash_map


def min_time_to_burn(root, target):
    # calling the node_parent_relation to get the
    # target Node and the node parent relation
    target_node, node_parent_map = node_parent_relation(root, target)

    # get the burn time using find_time function
    return find_time(target_node, node_parent_map)


root = inserttree()

print(min_time_to_burn(root, 2))
