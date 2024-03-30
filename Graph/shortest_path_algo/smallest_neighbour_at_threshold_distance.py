"""
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/
"""


def creat_adj_matrix(edges, n):
    # store all nodes as inf
    adj_matrix = [[float('inf') for _ in range(n)] for _ in range(n)]

    # updating the initial given weight of each node
    for u, v, distance in edges:
        adj_matrix[u][v] = distance
        adj_matrix[v][u] = distance

    # distance if u == v, will  be 0
    for i in range(n):
        adj_matrix[i][i] = 0

    return adj_matrix


def find_city(n, edges, distance_threshold):
    # create an adj matrix
    adj_matrix = creat_adj_matrix(edges, n)

    # usinf floyd warshall algo
    for via in range(n):
        for i in range(n):
            for j in range(n):
                adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][via] + adj_matrix[via][j])

    # now we need to count the number of cities reachable
    # from each cities under threshold value

    # this is used to get the count of cities under threshold at each row level
    cities_count = float('inf')

    # this will store the smallest no of cities that are reachable
    # through some path and whose distance is at most distance_threshold
    # intially keeping it -1
    result_city = -1

    for i in range(n):
        temp_city_count = 0
        for j in range(n):
            # if the distance is under threshold, use that city
            if adj_matrix[i][j] <= distance_threshold:
                temp_city_count += 1

        # if the current row smallest distance city count is less then current value
        # update the city count and the result city will be the current row city now
        if temp_city_count <= cities_count:
            cities_count = temp_city_count
            result_city = i

    return result_city

    """Below approach uses dictionary to get the result"""
    # cities_count = dict()
    # for i in range(n):
    #     for j in range(n):
    #         if adj_matrix[i][j] <= distance_threshold:
    #
    #             if cities_count.get(i):
    #                 cities_count[i] += 1
    #             else:
    #                 cities_count[i] = 1

    # print(cities_count)
    # cities_count = list(dict(sorted(cities_count.items(), key=lambda x: x[1], reverse=True)).keys())
    #
    # print(cities_count[-1])


n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4

n = 5
edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
distanceThreshold = 2
print(find_city(n, edges, distanceThreshold))
