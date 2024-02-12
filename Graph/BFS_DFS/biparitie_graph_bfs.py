from collections import deque


def bfs(adj, src, color, visited):
    dq = deque()

    dq.append(src)
    visited[src] = color

    while dq:
        source = dq.popleft()

        for vertex in adj[source]:

            if visited[vertex] == -1:
                # update color to opposite color
                visited[vertex] = 1 - visited[source]
                dq.append(vertex)

            elif visited[vertex] == visited[source]:
                return False

    return True


def bipartite_graph(adj):
    visited = [-1] * len(adj)

    for i in range(len(adj)):

        if visited[i] == -1:
            if not bfs(adj, i, 0, visited):
                return False

    return True


adj = [[1, 3], [0, 2], [1, 3], [0, 2]]
adj = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
adj = [[1], [0, 2], [1, 3, 5], [2, 4], [3, 7], [2, 6], [5, 7], [4, 6, 8], [7, 9], [8]]
adj = [[1], [0, 2, 3], [1, 5], [1, 4], [3, 5], [2, 4, 6], [5, 7], [6]]
print(bipartite_graph(adj))
