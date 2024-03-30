"""
Cycle Detection using BFS in Directed Graph
Tried: not working with my solution
"""

from collections import deque


def bfs(adj, source, visited, visiting):
    dq = deque()

    dq.append(source)
    visited[source] = 1
    visiting[source] = 1

    while dq:

        size = len(dq)
        temp = []
        for _ in range(size):
            source = dq.popleft()
            for vertex in adj[source]:
                temp.append(vertex)
                if visited[vertex] == -1:
                    dq.append(vertex)
                    visited[vertex] = 1

                elif visited[vertex] == 1 and visiting[vertex] == 1:
                    return True

        for x in temp:
            visiting[x] = 1



    return False



def detect_cycle(adj):
    visited = [-1] * len(adj)

    for i in range(len(adj)):

        if visited[i] == -1:
            visiting = [-1] * len(adj)
            if bfs(adj, i, visited, visiting) is True:
                return True

    return False

adj_matrix = [[1], [2], [3, 6], [4], [5], [], [4], [1, 8], [9], []]

print(detect_cycle(adj_matrix))
