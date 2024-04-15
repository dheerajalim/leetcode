def dfs(adj, source, visited, stack):
    visited[source] = True

    for vertex in adj[source]:

        if visited[vertex] is False:
            dfs(adj, vertex, visited, stack)

    stack.append(source)


def topo_sort(adj):
    visited = [False] * len(adj)
    stack = []
    for i in range(len(adj)):
        if visited[i] is False:
            dfs(adj, i, visited, stack)

    while stack:
        print(stack.pop(), end=" ")


adj = [[2, 3], [3, 4], [3], [], []]
topo_sort(adj)
