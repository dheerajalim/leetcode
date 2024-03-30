"""

Given the source and weighted graph, we need to find the shortest path form source
to all other nodes.

Steps:
1. Create a Adj Matrix with , this will be different as
    for example if there is edge between 0  and 1 and 0 and 2,
    we store the weight as well: [[1,23],[2,34]] # 23 and 34 are weights
2. Do the topo sort for the Graph
3. Maintain the distance list where initially all index will have inf stored and source will have 0
4. Now use the topo sort and calculate the shortest path
"""


def create_adj_matrix(n, edges):
    adj_matrix = [[] for _ in range(n)]
    # we are creating adj matrix as : where [[node, weight]]
    # [[[1, 2], [4, 1]], [[2, 3]], [[3, 6]], [], [[2, 2], [5, 4]], [[3, 1]]]
    for u, v, w in edges:
        adj_matrix[u].append([v, w])

    return adj_matrix


def topo_sort(adj_matrix):
    # using dfs to find topo sort
    def dfs(adj, source, visited, topo_sort_list):

        visited[source] = True
        # since we have weight as well at the index we use node, _ here
        for node, _ in adj[source]:
            if visited[node] is False:
                dfs(adj, node, visited, topo_sort_list)

        topo_sort_list.append(source)

    n = len(adj_matrix)
    visited = [False] * n
    topo_sort_list = []
    for i in range(n):
        if visited[i] is False:
            dfs(adj_matrix, i, visited, topo_sort_list)

    return topo_sort_list[::-1]
 

def shortest_path_dag(n, m, edges, src):
    """

    :param n: No. of vertices
    :param m: No. of Edges
    :param edges: List of Edges along with weight
    :return:
    """

    # create the adj matrix
    adj_matrix = create_adj_matrix(n, edges)

    # apply topo sort on the adj matrix

    topo_sort_list = topo_sort(adj_matrix)

    # create a distance matrix where each value will be
    # infinity and only source will be 0

    distance = [float('inf')] * n
    distance[src] = 0

    # now iterate through the adj matrix and relax the edges
    # we iterate through the order of topo sort
    for u in topo_sort_list:
        # the matrix store vertex v and the weight to reach v from u
        for v, weight in adj_matrix[u]:
            # if the current distance of vertex v is greater than new calculated distance
            # then we update the distance of vertex v to shorter distance
            # here the concept of topo is used as we will always find the shortest distance
            # in the first iteration, hence we need not update distance
            # for each path
            if distance[v] > distance[u] + weight:
                distance[v] = distance[u] + weight

    # for the question replace -1 to inf ( not required otherwise)
    for i in range(len(distance)):
        if distance[i] == float('inf'):
            distance[i] = -1

    return distance


edges = [[0, 1, 2], [0, 4, 1], [1, 2, 3], [2, 3, 6], [4, 2, 2], [4, 5, 4], [5, 3, 1]]
n = 6
m = len(edges)
src = 0

# edges = [[0, 1, 1], [1, 2, 3], [2, 3, 4], [1, 3, 2]]
# n = 4
# m = len(edges)
# src = 1

print(shortest_path_dag(n, m, edges, src))
