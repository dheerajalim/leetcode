"""
https://leetcode.com/problems/course-schedule-ii/description/
"""


def dfs(adj, source, visiting, visited):
    visited[source] = 1
    visiting[source] = 1
    for vertex in adj[source]:

        if visited[vertex] == -1:
            if dfs(adj, vertex, visiting, visited):
                return True

        elif visiting[vertex] == 1:
            return True

    visiting[source] = -1
    return False


def detect_cycle(adj):
    n = len(adj)
    visited = [-1] * n
    visiting = [-1] * n

    for i in range(n):

        if visited[i] == -1:
            if dfs(adj, i, visiting, visited):
                return True

    return False


adj = [[1], [2], [3, 6], [4], [5], [], [4], [1, 8], [9], [7]]
adj = [[1, 2], [0, 4], [0, 3, 5], [2], [1, 6], [2, 6], [4, 5]]
print(detect_cycle(adj))
