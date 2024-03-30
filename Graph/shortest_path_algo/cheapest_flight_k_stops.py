from collections import deque


def create_adj_matrix(flights, n):
    adj_matrix = [[] for _ in range(n)]

    for u, v, cost in flights:
        adj_matrix[u].append([v, cost])

    return adj_matrix


def cheapest_flights(n, flights, src, dst, k):
    """
    :param n: Number of cities
    """

    # create adj matrix

    adj = create_adj_matrix(flights, n)

    # create a cost list to gt the cheapest price
    total_cost = [float('inf') for _ in range(n)]
    # the cost to for the source is 0
    total_cost[src] = 0

    # the initial number of stops is 0
    stops = 0
    # now adding the source to the queue
    # we will be depending on the stop count
    # as that is what matters to reach dest in atmost k stops

    dq = deque()
    dq.append([stops, src, 0])

    while dq:

        current_stops, current_src, current_cost = dq.popleft()

        # as we have already crossed the limit of stops
        if current_stops > k:
            break
        # if we have reached then destination we can
        # continue to next item in queue as from this point
        # even if we move ahead it will increase cost as there are no negative cost
        if current_src == dst:
            continue

        for node, cost in adj[current_src]:

            if total_cost[node] > current_cost + cost:
                total_cost[node] = current_cost + cost
                dq.append([current_stops + 1, node, total_cost[node]])
    print(total_cost)
    return -1 if total_cost[dst] == float('inf') else total_cost[dst]


n = 5
flights = [[0, 1, 5], [0, 3, 2], [1, 2, 5], [1,4, 1], [3, 1, 2], [4, 2, 1]]
src = 0
dst = 2
k = 2



print(cheapest_flights(n, flights, src, dst, k))