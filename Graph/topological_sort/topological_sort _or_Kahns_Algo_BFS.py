"""
Topological Sorting (Kahn's BFS Based Algortihm)
> All the parent nodes are printed before its children
> That is nodes with lowes in-degree are printed first
> Works for the Directed Acyclic Graphs (DAG)


1. Find the in-degree of all the nodes
2. Add all the nodes with 0 indegree to queue
3. Traverse through the queue, and reduce the indegree by 1 for adj node
4. If the indegree of adj node become 0, enqueue it

USING BFS APPROACH
"""

from collections import deque


def get_indegree(adj_matrix):
    indegree_list = [0] * len(adj_matrix)

    for nodes in adj_matrix:
        for node in nodes:
            indegree_list[node] += 1

    return indegree_list


def kahns_algo(adj):
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

        print(current_node, end=" ")

        # now we will reduce the indegree for all the connected nodes
        # if the indegree becomes 0, then append it to the queue
        for node in adj[current_node]:
            indegree_list[node] -= 1
            if indegree_list[node] == 0:
                dq.append(node)


adj = [[2, 3], [3, 4], [3], [], []]
# adj = [[1, 2], [3], [3], [4, 5], [], []]

kahns_algo(adj)
