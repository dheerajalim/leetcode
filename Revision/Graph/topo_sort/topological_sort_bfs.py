"""
1. Count the inward edges for each node (indegree)
2. Push all the nodes with 0 inward edes to the queue
3. Whnever a node is reached, reduce its inward count
4. If the inward count becomes 0, add it to the queue

Whenever we pop from the queue, we print. This is the topo sort
This is used with Directed Acyclic Graph
"""

from collections import deque


def get_in_degree(adj):
    in_degree_count = [0] * len(adj)

    for i in range(len(adj)):

        for node in adj[i]:
            in_degree_count[node] += 1

    return in_degree_count


def topo_sort(adj):
    # get in degree of each node
    in_degree_count = get_in_degree(adj)

    dq = deque()

    for i in range(len(in_degree_count)):
        if in_degree_count[i] == 0:
            dq.append(i)

    while dq:

        source = dq.popleft()
        print(source, end=" ")

        for vertex in adj[source]:

            in_degree_count[vertex] -= 1
            if in_degree_count[vertex] == 0:
                dq.append(vertex)


adj = [[2, 3], [3, 4], [3], [], []]

topo_sort(adj)
