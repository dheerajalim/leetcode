"""
Used for finding the shortest path from a given source

1. Create a distance list where src is marked as 0, and all are initialized with inf
2. Now we take the source node and its distance and put it inside a min heap as [distance, src_node]
3. We relax the adjacent nodes from the min element of the heap
4. And push the nodes along with distance which were relaxed inside the min heap
5. Iterate above steps until heap is empty

"""
import heapq


def dijkstras_algo(adj, n, source):
    """ adj matrix = [[[node1, weight], [node2, weight]..]] will be like this"""

    # create a distance matrix
    distance = [float('inf') for _ in range(n)]

    # set the source distance as 0 : as it is 0 distance from itself
    distance[source] = 0

    # add the source distance inside min heap
    pq = [[0, source]]
    heapq.heapify(pq)

    while len(pq):

        source_weight, source_node = heapq.heappop(pq)

        # relax the adjacent nodes for the source_node
        # if the node distance is greater than source + edge weoght
        # then we update the node distance to a shorter distance
        for node, weight in adj[source_node]:
            if distance[node] > distance[source_node] + weight:
                distance[node] = distance[source_node] + weight
                heapq.heappush(pq, [distance[node], node])

    return distance


adj_matrix = [[[1, 4], [2, 4]], [[0, 4], [2, 2]], [[0, 4], [1, 2], [3, 3], [4, 1], [5, 6]], [[2, 3], [5, 2]],
              [[2, 1], [5, 3]], [[2, 6], [3, 2], [4, 3]]]
n = len(adj_matrix)
source = 0
print(dijkstras_algo(adj_matrix, n, source))