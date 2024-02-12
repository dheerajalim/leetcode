"""
Cycle Detection using DFS in Directed Graph
"""


def dfs(adj_matrix, source, visited, visiting):
    # now the source node is marked visited in global
    # and local scope
    visited[source] = 1
    visiting[source] = 1

    # use DFS for adjacent nodes
    for i in adj_matrix[source]:
        # if the node is not visited, call DFS recursively
        # we use visited here nad not visiting
        if visited[i] == -1:
            # if the cycle is detected return True
            if dfs(adj_matrix, i, visited, visiting) is True:
                return True

        # if the local path node is already visited,then this is a cycle
        if visiting[i] == 1:
            return True

    # after the recursion stack completes, update local path back to 1
    # this means that the current path can be revisited
    visiting[source] = -1
    return False


def detect_cycle(adj_matrix):
    # create the visited list for global path visit
    visited = [-1] * len(adj_matrix)
    # create visiting list for local path visit
    visiting = [-1] * len(adj_matrix)

    # iterate for all non visited nodes
    for i in range(len(adj_matrix)):
        if visited[i] == -1:
            if dfs(adj_matrix, i, visited, visiting) is True:
                return True

    return False


adj_matrix = [[1], [2], [3, 6], [4], [5], [], [4], [1, 8], [9], [7]]

print(detect_cycle(adj_matrix))
