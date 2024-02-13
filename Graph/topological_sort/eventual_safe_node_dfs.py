"""

If any node that is a part of cycle, then this is not goinf to be safe node
as we cannot reach the terminal node from nodes part of cycle i.e we can reach
but that's not the only path
"""


# this is the DFS algo for finding the cycle in directed graph
def dfs(adj, source, visited, visiting, safe_nodes):
    visited[source] = 1
    visiting[source] = 1

    for node in adj[source]:

        if visited[node] == -1:
            if dfs(adj, node, visited, visiting, safe_nodes):
                return True

        if visiting[node] == 1:
            return True

    visiting[source] = -1
    return False


def eventual_safe_nodes(graph):
    n = len(graph)
    visited = [-1] * n
    visiting = [-1] * n
    # to store the safe nodes
    safe_nodes = []

    # we need to check the path from all nodes
    # hence we will run for all nodes that are not visited
    for i in range(n):

        if visited[i] == -1:
            dfs(graph, i, visited, visiting, safe_nodes)

    # the -1 marked nodes in visiting array are the safe nodes
    # as they never formed cycle and reached terminal node
    # all cycle nodes will be marked 1
    for i in range(n):
        if visiting[i] == -1:
            safe_nodes.append(i)

    return sorted(safe_nodes)


graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
print(eventual_safe_nodes(graph))
