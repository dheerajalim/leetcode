"""
Find the shortest path between the node and
its connected edges

Works only in case of 1 unit distance between each node
"""
from collections import deque


def get_bfs(adj, source, visited, distance):
    # use the BFS traversal
    dq = deque()

    dq.append(source)
    visited[source] = True
    while dq:
        source = dq.popleft()

        for vertex in adj[source]:
            if visited[vertex] is False:
                dq.append(vertex)
                # increment the distance of vertex from source
                distance[vertex] = distance[source] + 1
                visited[vertex] = True


def shortest_path(adj, source):
    visited = [False] * len(adj)
    # initialize all the distance to inf initially
    distance = [float('inf')] * len(adj)

    # distance of source from source is 0
    distance[source] = 0

    get_bfs(adj, source, visited, distance)

    return distance


adj = [[1, 2], [0, 2, 3], [0, 1, 3], [1, 2]]

source = 0
print(shortest_path(adj, source))
