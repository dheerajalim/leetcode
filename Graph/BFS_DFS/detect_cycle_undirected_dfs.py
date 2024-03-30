"""
Detect cycle in Undirected Graph using DFS
"""


def dfs(adj, source, visited, parent):
    # mark the source as visited
    visited[source] = True
    # iterate through all the vertex of the source
    for vertex in adj[source]:
        # if the vertex is not visisted
        # recursively call the DFS on this vertex with parent as source
        if visited[vertex] is False:
            return dfs(adj, vertex, visited, source)
        # else if this vertex is already visited and is not
        # a parent vertex, this is a cycle
        # as a vertex was already touched by some other path
        elif visited[vertex] is True and vertex != parent:
            return True

    return False


# for disconnected graph with no source input
def detect_cycle(adj):
    visited = [False] * len(adj)
    # iterate trhough all the vertices
    for i in range(len(adj)):
        # if the vertex is not visited , call the
        # DFS for that vertex as source
        if visited[i] is False:
            # the source parent is always -1
            parent = -1
            # call the dfs for the source which is not visisted
            if dfs(adj, i, visited, parent):
                return "Cycle Detected"

    return False


adj = [[1, 2], [0, 4], [0, 3, 5], [2], [1, 6], [2, 6], [4, 5]]
print(detect_cycle(adj))
