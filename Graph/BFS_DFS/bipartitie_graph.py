"""
graph that can have all adjacent nodes in alternate color
"""


def dfs(src, color, visited, adj):
    # mark the src node as visited with color 0
    visited[src] = color

    # iterate through all adjacent node of src
    for i in adj[src]:
        # if the node is not colored yet, color it in opposite color
        # compared to src and add it to the queue
        if visited[i] == -1:
            # if the DFS get a False, we just return it as the graph is already marked non-bipartite
            if dfs(i, 1 - color, visited, adj) is False:
                return False
        # else if the node is already visited and its color is same as
        # source color, then this is not a bipartite graph; return False
        elif visited[i] == visited[src]:
            return False

    return True


def check_bipartite(adj):
    # mark all the nodes color as -1
    visited = [-1] * len(adj)

    for i in range(len(adj)):
        # iterate all the node which are not yet colored/not visisted
        if visited[i] == -1:
            # call DFS on the nodes, pass the src node with color 0
            result = dfs(i, 0, visited, adj)
            if result is False:
                return result

    return True


adj = [[1], [0, 2, 3], [1, 5], [1, 4], [3, 5], [2, 4, 6], [5, 7], [6]]

# adj = [[1], [0, 2], [1, 3, 5], [2, 4], [3, 7], [2, 6], [5, 7], [4, 6, 8], [7, 9], [8]]

# adj = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
adj = [[1, 3], [0, 2], [1, 3], [0, 2]]

print(check_bipartite(adj))
