"""
https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/
"""

from collections import deque


def edges_to_adj_list(edges, n):
    v = n  # vertices
    adj_list = [[] for _ in range(v)]

    for i, j in edges:
        adj_list[i].append(j)
        adj_list[j].append(i)

    return adj_list


def bfs(adj, src, visited):
    dq = deque()
    visited[src] = True
    connected_component_vertex = 1
    dq.append(src)

    while dq:
        source = dq.popleft()
        for vertex in adj[source]:

            if visited[vertex] is False:
                dq.append(vertex)
                visited[vertex] = True
                connected_component_vertex += 1

    return connected_component_vertex


def unreachable_pairs(n, edges):
    adj_list = edges_to_adj_list(edges, n)
    connected_component_count = []
    visited = [False] * n
    for i in range(len(adj_list)):

        if visited[i] is False:
            connected_component_vertex_count = bfs(adj_list, i, visited)
            connected_component_count.append(connected_component_vertex_count)

    total_vertex = n
    num_unreachable_pairs = 0
    # formula :  ans = ans + (connected_graph_nodes * [total_nodes - connected_graph_nodes])
    # update total nodes as well : total_nodes = total_nodes - connected_graph_nodes
    for nodes_count in connected_component_count:
        num_unreachable_pairs += nodes_count * (total_vertex - nodes_count)
        total_vertex = total_vertex - nodes_count

    return num_unreachable_pairs


n = 7
edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]

print(unreachable_pairs(n, edges))
