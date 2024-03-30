"""

This algo is a brute force approach to get the shortest from each node to another node
The response is a dj matrix which stores the shortest path of all the n nodes

If a negative weight cycle exists then the shortest path will be less than 0

The input is an adj matrix that has the edge weight for a[i][j] = weight
For the same vertex the weight will be 0, a[i][i]=0
If there is no edge from i to j , then it is inf, (i.e unreachable)
"""


def floyd_warshall(adj_matrix):
    # total number of nodes
    n = len(adj_matrix)

    # as we will go from each node as a in between stop
    for via in range(n):

        # for each edge , we will take the minimum weight
        # between the existing weight and the new weight achieved via another stop
        for i in range(n):
            for j in range(n):
                adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][via] + adj_matrix[via][j])

    # if we need to detect the negative cycle
    # which means that the weight of a[i][i] < 0
    # the same node can be reached in distance < 0 which makes it clear
    # that a negative cycle  exists
    for i in range(n):
        if adj_matrix[i][i] < 0:
            return 'Contains Negative Cycle'

    # return the adj matrix with the shortest path between each node
    return adj_matrix


adj_matrix = [[0, 1, 43], [1, 0, 6], [float('inf'), float('inf'), 0]]
# to check negative cycle
# adj_matrix = [[0, -1, 43], [-1, 0, -6], [float('inf'), float('inf'), 0]]

print(floyd_warshall(adj_matrix))
