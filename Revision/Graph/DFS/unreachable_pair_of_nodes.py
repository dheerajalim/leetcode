"""
https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/
"""


def edges_to_list(n, edges):
    adj_list = [[] for _ in range(n)]

    for i, j in edges:
        adj_list[i].append(j)
        adj_list[j].append(i)

    return adj_list


def dfs(adj, source, visited, count):
    visited[source] = True
    count[0] += 1
    for vertex in adj[source]:

        if visited[vertex] is False:
            visited[vertex] = True
            dfs(adj, vertex, visited, count)


def count_pairs(n, edges):
    adj_list = edges_to_list(n, edges)

    visited = [False] * n
    connected_count = []
    for i in range(n):
        if visited[i] is False:
            count = [0]
            dfs(adj_list, i, visited, count)
            connected_count.append(count[0])

    total_edges = n
    pairs = 0
    for count in connected_count:
        pairs += count * (total_edges - count)
        total_edges = total_edges - count

    return pairs


n = 7
edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]

n = 3
edges = [[0, 1], [0, 2], [1, 2]]

print(count_pairs(n, edges))
