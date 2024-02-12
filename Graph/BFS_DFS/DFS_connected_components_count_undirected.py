"""
Give the total number of connected graphs using DFS
"""


def get_dfs(adj, source, visited):
    visited[source] = True

    for i in adj[source]:
        if visited[i] is False:
            get_dfs(adj, i, visited)


def DFS(adj):
    visited = [False] * len(adj)
    # maintain a count variable to get the
    # unconnected graph count
    count = 0
    # iterate through each of the vertex
    for i in range(len(adj)):
        # if the vertex is not visisted
        # pass that as the source and run DFS
        if visited[i] is False:
            # increment the count for the source vertex
            # which initiates DFS
            count += 1
            get_dfs(adj, i, visited)

    return count


adj = [[1, 2], [0, 2], [0, 1], [4], [3]]
print(DFS(adj))
