"""
https://leetcode.com/problems/find-center-of-star-graph/description/
A star graph is a graph where there is one center node and exactly
n - 1 edges that connect the center node with every other node.

Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
"""


def find_center(edges):
    n_edges = len(edges)
    n_vertices = n_edges + 1
    # since the vertices start from 1 to n, we use n+1 to avoid 0
    degree = [0] * (n_vertices + 1)

    for u, v in edges:
        degree[u] += 1
        if degree[u] == n_edges:
            return u

        degree[v] += 1
        if degree[v] == n_edges:
            return v


edges = [[1,2],[5,1],[1,3],[1,4]]
print(find_center(edges))