from binary_tree import *

from collections import deque


# Similar to the algo for Minimum time to burn
def parent_mapping(root, target):
    # following the level order traversal algo
    # to store parent - node relation
    mapping = {}
    # to store the target node as the give value is integer
    target_node = None
    dq = deque()
    dq.append(root)

    while dq:

        current = dq.popleft()
        # to check if the current node data is equal to
        # the target node
        if current.data == target:
            target_node = current
        # level order algo steps
        if current.left:
            dq.append(current.left)
            mapping[current.left] = current
        if current.right:
            dq.append(current.right)
            mapping[current.right] = current

    # return the parent-node relation hash map and the
    # target node
    return mapping, target_node


def find_nodes(target_node, k, mapping):
    # store the already visited node
    # this is useful as it is possible that our target node
    # is the parent or left/right of some other node in the tree
    # then if the node is already visited we ignore that for k distance

    # the target node is already visited, hence update the
    # visited hash map
    visited = {target_node: 1}
    dq = deque()
    # starting from the target node, hence add it to queue
    # similar to level order traversal
    dq.append(target_node)

    while dq:
        size = len(dq)
        # follow the level order line by line algo
        for _ in range(size):
            current = dq.popleft()
            # if the left node exist and is not visited
            if current.left and not visited.get(current.left):
                dq.append(current.left)
                # add to queue, mark it visited
                visited[current.left] = 1
            # if the right node exist and is not visited
            if current.right and not visited.get(current.right):
                dq.append(current.right)
                # add to queue, mark it visited
                visited[current.right] = 1

            # this condition is for the parent node
            # which is also a possibility for node at k distance
            if mapping.get(current) and not visited.get(mapping.get(current)):
                dq.append(mapping[current])
                visited[mapping[current]] = 1

        # after 1 level, we reduce the k by 1
        k -= 1
        # if k ==0 , then we have reached at k distance from the target node
        if k == 0:
            return dq

    # else we did not find any nodes
    return []


def nodes_at_k(root, target, k):
    if root is None:
        return []
    # if the distance to find nodes is 0, then target is the answer
    if k == 0:
        return target

    mapping, target_node = parent_mapping(root, target)

    at_k_distance = find_nodes(target_node, k, mapping)
    result = []
    # parse the nodes in queue and create a new kist with
    # nodes.data
    for i in at_k_distance:
        result.append(i.data)

    return result


root = inserttree()
target = 5
k = 2
print(nodes_at_k(root, target, k))
