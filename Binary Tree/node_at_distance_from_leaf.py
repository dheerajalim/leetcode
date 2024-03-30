from binary_tree import *

from collections import deque


# using the level order traversal and queue
def parent_map(root):
    # using this function we get the parent mapping for each
    # node. Also we get all the leaf nodes from this function
    # when both left and right nodes are None, then this is leaf Node
    if root is None:
        return

    dq = deque()
    dq.append(root)
    # to store the mapping
    hash_map = dict()
    # to store the leaf nodes
    leaf_nodes = deque()
    while dq:

        current = dq.popleft()

        if current.left:
            dq.append(current.left)
            hash_map[current.left] = current

        if current.right:
            dq.append(current.right)
            hash_map[current.right] = current
        # gives the leaf nodes
        if not current.left and not current.right:
            leaf_nodes.append(current)

    return hash_map, leaf_nodes


def get_count(root, k, mapping, leaf_nodes):
    if root is None:
        return
    result_count = 0
    # to mark if the node at distance k is already visited
    visited = dict()
    # we iterate over all the leaf nodes
    while leaf_nodes:
        # get the leaf node from queue front
        current = leaf_nodes.popleft()
        flag = 0
        # then we search for it parent at k nodes above it
        # using the parent mapping relation
        for i in range(k):
            # if we find it, then we set flag to 1
            if mapping.get(current):
                parent = mapping[current]
                current = parent
                flag = 1
            # otherwise we set flag to 0
            else:
                flag = 0
        # if flag is 1 and the node at k distance above leaf
        # is not visited already we increment count
        # and set the visited to true for that node
        if flag and not visited.get(current):
            result_count += 1
            visited[current] = 1

    return result_count


def printKDistantfromLeaf(root, k):
    if root is None:
        return None

    mapping, leafnodes = parent_map(root)
    # this means that all the leaf nodes are themselves the
    # result as they are at o distance from leaf
    if k == 0:
        return len(leafnodes)
    return get_count(root, k, mapping, leafnodes)


root = inserttree()
k = 4
print(printKDistantfromLeaf(root, k))
