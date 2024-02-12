from collections import deque


def bfs(adj, source, visited):
    dq = deque()

    dq.append(source)
    visited[source] = True

    while dq:

        source = dq.popleft()
        for vertex in adj[source]:
            if visited[vertex] is False:
                dq.append(vertex)
                visited[vertex] = True


def bfs_connected_count(adj):
    visited = [False] * len(adj)
    count = 0
    for v in range(len(adj)):
        if visited[v] is False:
            # whenever a non connected graph comes
            # we increment the count
            count += 1
            bfs(adj, v, visited)
    return count

adj = [[1, 2], [0, 2], [0, 1], [4], [3], [6, 7], [5, 7], [5, 6]]
print(bfs_connected_count(adj))