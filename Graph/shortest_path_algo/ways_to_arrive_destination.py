"""
whenever the destination is arrived, we
check if the this distance is less than prev shortest dist,
then we restart count from 1
else if the new distance is equal to shortest : count ++
if greater than shortest , ignore

"""

import heapq


def create_adj_list(roads, n):
    adj_list = [[] for _ in range(n)]

    for u, v, time in roads:
        adj_list[u].append([v, time])
        adj_list[v].append([u, time])

    return adj_list


def count_path(n, roads):
    adj = create_adj_list(roads, n)

    src, dst = 0, n - 1

    pq = [[0, src]]

    heapq.heapify(pq)

    distance = [float('inf') for _ in range(n)]
    distance[src] = 0

    ways = [0] * n
    ways[src] = 1


    while pq:
        current_time, current_source = heapq.heappop(pq)

        # if we reached the destination we can skip moving iteration
        # as we have already reached the destination and moving further will
        # will only increase the time
        if current_source == dst:
            break

        for node, time in adj[current_source]:

            if distance[node] == time + current_time:
                ways[node] += ways[current_source]

            elif distance[node] > time + current_time:
                distance[node] = time + current_time
                heapq.heappush(pq, [distance[node], node])

                ways[node] = ways[current_source]

    return ways[-1] % (10 ** 9 + 7)


roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
n = 7

# roads = [[1, 0, 10]]
# n = 2

print(count_path(n, roads))
