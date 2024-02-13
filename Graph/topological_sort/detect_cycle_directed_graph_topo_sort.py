"""
Since TOPO sort is only valid for DAG, hence we use it to check
if the directed graph is cyclic or acyclic

If the indegree of all items become 0, then this is acyclice
else cyclic
"""

from collections import deque


def get_indegree(adj_matrix):
    indegree_list = [0] * len(adj_matrix)

    for nodes in adj_matrix:
        for node in nodes:
            indegree_list[node] += 1

    return indegree_list


def cycle_detection(adj):
    # get the indegree of each node
    indegree_list = get_indegree(adj)

    # adding the 0 indegree nodes to queue
    # finding the nodes with 0 indegree and pushing them to queue
    # as they are the starting point of topo sort
    dq = deque()

    for i in range(len(indegree_list)):
        if indegree_list[i] == 0:
            dq.append(i)

    # now dq will have all nodes that have 0 in degree
    while dq:
        # take the left item from queue and print
        current_node = dq.popleft()

        # now we will reduce the indegree for all the connected nodes
        # if the indegree becomes 0, then append it to the queue
        for node in adj[current_node]:
            indegree_list[node] -= 1
            if indegree_list[node] == 0:
                dq.append(node)

    # this means that a cycle exists
    if sum(indegree_list) > 0:
        return True

    return False


adj = [[1], [2], [3, 6], [4], [5], [], [4], [1, 8], [9], [7]]

print(cycle_detection(adj))
