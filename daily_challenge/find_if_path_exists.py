"""
https://leetcode.com/problems/find-if-path-exists-in-graph/description/?envType=daily-question&envId=2024-04-21
"""


def get_adj_list(n, edges):
    adj_list = [[] for _ in range(n)]

    for i, j in edges:
        adj_list[i].append(j)
        adj_list[j].append(i)

    return adj_list


def dfs(adj, source, destination, visited):
    visited[source] = True

    # since we need to check if we can reach the destination
    # as we keep on moving in Graph,our source keeps on updating, as we started from given source
    # and if we were able to reach the destination , we stop and return true
    if source == destination:
        return True

    for vertex in adj[source]:

        if visited[vertex] is False:
            if dfs(adj, vertex, destination, visited):
                return True

    return False


def valid_path(n, edges, source, destination):
    adj_list = get_adj_list(n, edges)

    visited = [False for _ in range(n)]
    # using standard DFS
    if visited[source] is False:
        return dfs(adj_list, source, destination, visited)


n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2

print(valid_path(n, edges, source, destination))
