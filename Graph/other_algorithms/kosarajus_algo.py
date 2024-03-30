"""
1. Sort all the edges based on finish time
yhe step allow krta hai to understand ki kaunsa node sc1 ko belong krta hai
jo node stack ke top pe hoga wahin se start krenge
2. Reverse the graph
3. Do DFS
"""


def dfs(adj, src, visited, stack):
    visited[src] = True

    for node in adj[src]:
        if visited[node] is False:
            dfs(adj, node, visited, stack)

    stack.append(src)


def dfs_scc(adj, src, visited, scc_nodes):
    # this is general dfs algo
    visited[src] = True

    for node in adj[src]:
        if visited[node] is False:
            dfs_scc(adj, node, visited, scc_nodes)

    # store the scc nodes
    scc_nodes.append(src)


def kosaraju(n, adj_list):
    visited = [False] * n
    # to store the nodes and get to know the node of first component
    stack = []

    # Step 1 : Get the nodes of the graph in sorted order based on finish time
    for i in range(n):
        if visited[i] is False:
            dfs(adj_list, i, visited, stack)

    # Step 2 : Reverse the edges of the graph
    adj_list_reverse = [[] for _ in range(n)]

    for u, nodes in enumerate(adj_list):
        for v in nodes:
            adj_list_reverse[v].append(u)

    # Step 3 : Start the DFS on the sorted nodes

    visited = [False] * n
    # to store the count of scc
    scc = 0
    # to store all the scc path
    all_scc_nodes = []
    # we take the nodes from the stacks top
    # as the top element of stack is the part of first scc
    while stack:
        i = stack[-1]
        stack.pop()
        if visited[i] is False:
            scc += 1
            # to store the scc path of single component
            scc_nodes = []
            dfs_scc(adj_list_reverse, i, visited, scc_nodes)
            all_scc_nodes.append(scc_nodes)

    return scc, all_scc_nodes


n = 8
adj_list = [[1], [2], [0, 3], [4], [5, 7], [6], [4, 7], []]

print(kosaraju(n, adj_list))
