"""
DFS Traversal
"""


def dfs(adj_list, source, visited):

    visited[source] = True
    print(source)

    for vertex in adj_list[source]:
        if visited[vertex] is False:

            dfs(adj_list, vertex, visited)


def traversal(adj_list):

    n = len(adj_list)

    visited = [False] * n

    for i in range(len(adj_list)):
        if visited[i] is False:
            dfs(adj_list, i, visited)


adj = [[1, 2], [0, 2], [0, 1], [4], [3]]
traversal(adj)