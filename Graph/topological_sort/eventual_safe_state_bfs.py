"""
Since we need to find path to reach terminal node,
 Let reverse this: why don't we start
with terminal node, and all nodes that can be reached from terminal nodes are safe nodes
We can use topo sort, any node with a cycle will be not a part of path
Steps:
1. Convert all outward nodes to inward( for topo sort)
2. Follow the topo sort
3. Store the node after poping from queue to a list (topo_sort_list)
4. The nodes in topo_sort_list are safe nodes
"""

from collections import deque


def outward_to_inward(adj):
    inward_adj = [[] for _ in range(len(adj))]

    indegree_list = [0] * len(adj)

    for node in range(len(adj)):
        for outward_nodes in adj[node]:
            inward_adj[outward_nodes].append(node)
            indegree_list[node] += 1

    return inward_adj, indegree_list


# def get_indegree(adj_matrix):
#     indegree_list = [0] * len(adj_matrix)
#
#     for nodes in adj_matrix:
#         for node in nodes:
#             indegree_list[node] += 1
#
#     return indegree_list


def eventual_safe_nodes(graph):
    inward_adj,indegree_list = outward_to_inward(graph)

    # indegree_list = get_indegree(inward_adj)

    dq = deque()

    # adding all the terminal nodes to queue
    for i in range(len(indegree_list)):
        if indegree_list[i] == 0:
            dq.append(i)

    # list to contain the nodes that were reached from terminal nodes
    topo_sort = []

    # now dq will have all nodes that have 0 in degree
    while dq:
        # take the left item from queue and print
        current_node = dq.popleft()

        topo_sort.append(current_node)

        # now we will reduce the indegree for all the connected nodes
        # if the indegree becomes 0, then append it to the queue
        for node in inward_adj[current_node]:
            indegree_list[node] -= 1
            if indegree_list[node] == 0:
                dq.append(node)
    print(indegree_list)
    return sorted(topo_sort)


graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]

print(eventual_safe_nodes(graph))
