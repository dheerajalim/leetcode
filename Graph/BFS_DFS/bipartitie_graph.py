"""
graph that can have all adjacent nodes in alternate color
"""


def dfs(src, color, visited, adj):

    visited[src] = color

    for i in adj[src]:
        if visited[i] == -1:

            if dfs(i, 1 -  color, visited, adj) is False:
                return False

        elif visited[i] == visited[src]:
            return False

    return True


def check_bipartite(adj):
    visited = [-1] * len(adj)

    for i in range(len(adj)):
        if visited[i] == -1:
            result = dfs(i, 0, visited, adj)
            if result is False:
                return result

    return True


adj = [[1], [0, 2, 3], [1, 5], [1, 4], [3, 5], [2, 4, 6], [5, 7], [6]]

# adj = [[1], [0, 2], [1, 3, 5], [2, 4], [3, 7], [2, 6], [5, 7], [4, 6, 8], [7, 9], [8]]

# adj = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
adj = [[1, 3], [0, 2], [1, 3], [0, 2]]

print(check_bipartite(adj))
