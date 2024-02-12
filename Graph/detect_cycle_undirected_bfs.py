"""
Detect cycle in Undirected Graph using BFS
"""

from collections import deque


def bfs(adj, source, visited):
    dq = deque()
    # for the initial source, we assume parent as -1
    dq.append([source, -1])
    # mark this source as visited
    visited[source] = True
    while dq:
        source, parent = dq.popleft()
        # iterating through all the vertex of the source
        for vertex in adj[source]:
            # if the vertex is visited and is parent vertex
            # then we continue
            if visited[vertex] is True and parent == vertex:
                continue
            # if the vertex is visited and is not parent vertex
            # then it's a cycle
            elif visited[vertex] is True and parent != vertex:
                return True
            # else, we add the non visited vertex to the queue
            # mark it as visited
            elif visited[vertex] is False:
                visited[vertex] = True
                dq.append([vertex, source])

    # else return False for no cycle detection
    return False


def detect_cycle(adj):
    visited = [False] * len(adj)
    # run iteration for all the vertices
    for i in range(len(adj)):
        if visited[i] is False:
            # if bfs returns true, then it's a cycle
            if bfs(adj, i, visited):
                return "Cycle Detected"
    # else return false
    return False


adj = [[1, 2], [0, 4], [0, 3, 5], [2], [1, 6], [2, 6], [4, 5]]
adj = [[1, 2], [0, 4], [0, 3, 5], [2], [1, 6], [2], [4], [8, 9], [7, 9], [7, 8]]

print(detect_cycle(adj))
