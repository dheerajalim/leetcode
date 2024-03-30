"""
1. Create a Visited Array, to store the vertices/nodes that are visited
2. A min heap that will store the [weight, node, parent]
3. Any node can be taken as source and its parent will be -1.
4. We keep the parent node here in case ,we need the MST edges as well
5. Iterate until the min heap is empty.
6. Pop the item from min heap and if it is not already visited:
    a. Then add its weight to the result variable
    b. Mark this node as visited in the visisted array
7. Iterate through its adjacent nodes and check if the node is visited, if not then add this node to the min heap.
8. Return the res (which has the weight of MST) and if required return the MST path
"""

import heapq


def create_adj_list(n, edges):
    # creating a undirected adj list
    adj_list = [[] for _ in range(n)]

    for u, v, weight in edges:
        adj_list[u].append([v, weight])
        adj_list[v].append([u, weight])

    return adj_list


def prims_algo(n, edges):
    # create a adj list for undirected graph
    adj_list = create_adj_list(n, edges)

    # create a visited array
    visited = [False] * n

    # to store the weight of MST
    res = 0

    # this is a min heap to get the minimum weight edge
    distance_pq = []

    # to store the path of MST
    mst = []

    # the initial node , we are taking is 0 node, and we push its distance as 0
    # it is [weight, node, parent] and parent is -1  for inital node
    heapq.heappush(distance_pq, [0, 0, -1])

    while distance_pq:

        current_weight, current_node, parent = heapq.heappop(distance_pq)

        # if the node is already visited or part of MST, we ignore the iteration
        # as the node is already a part of MST, and we do not need to process its adjacent
        if visited[current_node]:
            continue

        # else mark it visited by adding it to our MST
        else:
            visited[current_node] = True

        # take this node and add its weight to our MST weight
        res += current_weight
        # to store the MST path, we ignore the initial node
        if parent != -1:
            mst.append([parent, current_node])

        # check for the adjacent nodes of the current node
        for node, weight in adj_list[current_node]:
            # if the adjacent node is not visisted we add it to the min heap
            if visited[node] is False:
                heapq.heappush(distance_pq, [weight, node, current_node])

    # this is the sum of MST weight
    print(res)
    # this is the MST path
    print(mst)


n = 5
edges = [[0, 1, 2], [0, 3, 6], [1, 2, 3], [1, 3, 8], [1, 4, 5], [4, 2, 7]]

prims_algo(n, edges)
