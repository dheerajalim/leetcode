"""

Use DJ based on time as the shortest path
"""

import heapq


def create_adj_list(times, n):
    # times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]

    adj_list = [[] for _ in range(n + 1)]

    for u, v, time in times:
        adj_list[u].append([v, time])

    return adj_list


def network_delay(times, n, k):
    # create adj list

    adj = create_adj_list(times, n)

    # create a distance list
    distance = [float('inf') for _ in range(n + 1)]

    # source is k
    src = k
    distance[src] = 0

    # create a min heap
    pq = [[0, src]]
    heapq.heapify(pq)

    while len(pq):

        current_time, current_src = heapq.heappop(pq)
        # if the time of node is > then time taken to reach here from src
        # then update the time of ode
        for node, time in adj[current_src]:
            if distance[node] > current_time + time:
                distance[node] = current_time + time
                heapq.heappush(pq, [distance[node], node])

    # if any of the node was not visited, then we return -1
    if float('inf') in distance[1:]:
        return -1
    # else the max time will be the time we need to wait to make signal reach everyone
    return max(distance[1:])


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
# times = [[1, 2, 1]]
# times = [[1,2,1],[2,3,2],[1,3,4]]
n = 4
k = 2

print(network_delay(times, n, k))
