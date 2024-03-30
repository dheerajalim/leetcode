"""
Topological Sorting (Kahn's BFS Based Algortihm)
> All the parent nodes are printed before its children
> That is nodes with lowes in-degree are printed first
> Works for the Directed Acyclic Graphs (DAG)

Step 1 : Choose any starting Node and a visited List
Step 2 : Run the DFS on that node and mark the related nodes as visisted
Step 3 : At the recursion stack backtrack , add the nodes to a stack
Step 4 : The items in the stak when poped one by pne are the topo sort order
"""


def dfs(adj, source, visited, topo_sort):
    # this is DFS algo; only difference is that
    # while backtracking recursion stack, we append the
    # source to top_sort stack
    visited[source] = True

    for node in adj[source]:
        if visited[node] is False:
            dfs(adj, node, visited, topo_sort)

    topo_sort.append(source)


def kahns_algo(adj):
    # create a visited array, to track visited nodes
    visited = [False] * len(adj)
    # this stack to store the sort order
    topo_sort = []
    # iterate through the nodes
    for i in range(len(adj)):
        # call DFS on non visited node
        if visited[i] is False:
            dfs(adj, i, visited, topo_sort)

    # pop the items from the stack, this is the topo sort
    while topo_sort:
        print(topo_sort.pop(), end=" ")


adj = [[2, 3], [3, 4], [3], [], []]
# adj = [[1], [3], [3,4], [4], []]
adj =  [[1], [2], [3, 6], [4], [5], [], [4], [1, 8], [9], [7]]
kahns_algo(adj)
