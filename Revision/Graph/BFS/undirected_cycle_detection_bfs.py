from collections import deque


def has_cycle(adj, visited, source):
    dq = deque()

    dq.append([source, -1])

    visited[source] = True

    while dq:

        source, parent = dq.popleft()

        for vertex in adj[source]:

            if visited[vertex] is True and vertex == parent:
                continue

            elif visited[vertex] is True and vertex != parent:
                return True

            else:
                visited[vertex] = True
                dq.append([vertex, source])

    return False


def detect_cycle(adj):
    n = len(adj)

    visited = [False] * n

    for i in range(n):

        if visited[i] is False:
            if has_cycle(adj, visited, i):
                return "Cycle Detected"

    return "No Cycle Detected"


adj = [[1, 2], [0, 4], [0, 3, 5], [2], [1, 6], [2, 6], [4, 5]]
print(detect_cycle(adj))