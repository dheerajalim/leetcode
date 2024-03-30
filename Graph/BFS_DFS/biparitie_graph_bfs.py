from collections import deque


def bfs(adj, src, color, visited):
    dq = deque()

    dq.append(src)
    # mark the src node as visited with color 0
    visited[src] = color

    while dq:
        source = dq.popleft()
        # iterate through all adjacent node of src
        for vertex in adj[source]:
            # if the node is not colored yet, color it in opposite color
            # compared to src and add it to the queue
            if visited[vertex] == -1:
                # update color to opposite color
                visited[vertex] = 1 - visited[source]
                dq.append(vertex)
            # else if the node is already visited and its color is same as
            # source color, then this is not a bipartite graph; return False
            elif visited[vertex] == visited[source]:
                return False

    return True


def bipartite_graph(adj):
    # mark all the nodes color as -1
    visited = [-1] * len(adj)

    for i in range(len(adj)):
        # iterate all the node which are not yet colored/not visisted
        if visited[i] == -1:
            # call bfs on the nodes, pass the src node with color 0
            if not bfs(adj, i, 0, visited):
                return False

    return True


adj = [[1, 3], [0, 2], [1, 3], [0, 2]]
adj = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
adj = [[1], [0, 2], [1, 3, 5], [2, 4], [3, 7], [2, 6], [5, 7], [4, 6, 8], [7, 9], [8]]
adj = [[1], [0, 2, 3], [1, 5], [1, 4], [3, 5], [2, 4, 6], [5, 7], [6]]
print(bipartite_graph(adj))
