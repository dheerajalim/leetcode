"""
TC : O(V + E)
"""


def DFS_connected_graph(adj, source, visited):
    # print the source vertex
    print(source, end=" ")
    # update the visisted for source vertex to true
    visited[source] = True

    # iterate through all the adj vertex of source
    for i in adj[source]:
        # if the adj vertex is not visited,
        # recursively call the DFS for that vertex
        if visited[i] is False:
            DFS_connected_graph(adj, i, visited)


adj = [[1, 4], [0, 2], [1, 3], [2], [0, 5, 6], [4, 6], [4, 5]]
source = 0
visited = [False] * len(adj)

DFS_connected_graph(adj, source, visited)


def DFS_disconnected_graph(adj, source, visited):
    print(source, end=" ")
    visited[source] = True
    for i in adj[source]:
        if visited[i] is False:
            DFS_connected_graph(adj, i, visited)


# for disconnected graph with no source input
def get_dfs(adj):
    visited = [False] * len(adj)
    # iterate trhough all the vertices
    for i in range(len(adj)):
        # if the vertex is not visited , call the
        # DFS for that vertex as source
        if visited[i] is False:
            DFS_disconnected_graph(adj, i, visited)


print('---')
adj = [[1, 2], [0, 2], [0, 1], [4], [3]]
adj = [[1],[0,2,3],[1,4],[1,5],[2,6],[3,2],[4,7],[6]]
get_dfs(adj)
