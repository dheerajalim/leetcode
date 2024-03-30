"""
Finds the shortest path

The idea is that we can get the shprtes path to each vertex in max V-1 iterations
So after V-1 iterations, the distance of each vertex from source is the shortest distance

Note : This works with negative weights and detects negative weight cycle as well
Note : This works with only Directed Graphs, and if we want to use it for undirected, create
        two directed edges between a pair of vertices
Note : The edges can be given in any order, so Bellman ford still works fine, we do not need to have the order of edges

1. Create a distance list to store the distance
2. Calculate the number of vertices and create a loop for V-1 iterations
3. Use the relax operation in each iteration
4. After V-1 iterations we run for one more time the iteration, this is a safety measure to ensure that there are no
   negative weight cycles
"""


def bellman_ford(src, n, edges):
    # n is the number of vertices, hence we need to run n-1 iteration
    iterations = n - 1

    # create a distance list with source disatnce as 0
    distance = [float('inf') for _ in range(n)]
    # the source ndoe will be at 0 distance
    distance[src] = 0

    i = 0

    # we run the relax operation on each node V-1 times
    while i < iterations:
        # here we run the relax operation on all the nodes
        for u, v, weight in edges:
            # this condition distance[u] != float('inf') is checked , since if the previous node itself
            # is infinity then checking it for shorter distance of next node is of no sense
            if distance[u] != float('inf') and distance[v] > distance[u] + weight:
                distance[v] = distance[u] + weight
        i += 1

    # this is one more time relax operation on each node, to check if negative
    # weight cycle exists, if it does, then it will further reduce the weights
    for u, v, weight in edges:

        if distance[u] != float('inf') and distance[v] > distance[u] + weight:
            print("Negative Weight Cycle")

    return distance


# this can be given in any order
edges = [[1, 2, -3], [0, 1, 1], [0, 2, 4], [1, 3, 2], [2, 3, 3]]
n = 4
src = 0

# # Example for negative weight cycle
# edges = [[0, 1, 4], [0, 2, 8], [1, 2, -8], [2, 3, 2], [3, 1, 3]]
# src = 0
# n = 4
print(bellman_ford(src, n, edges))
