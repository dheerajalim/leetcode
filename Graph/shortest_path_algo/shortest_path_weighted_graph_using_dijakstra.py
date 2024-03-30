import heapq


def create_adj_matrix(edges, n):
    adj_matrix = [[] for _ in range(n)]

    for u, v, w in edges:
        adj_matrix[u].append([v, w])
        adj_matrix[v].append([u, w])

    return adj_matrix


def dijkstras_algo(edges, n, m):
    # source is always 0

    distance = [[float('inf'), i] for i in range(n)]
    # distance = [[float('inf'), float('inf')] for _ in range(n)] # case where we store default parent as inf
    distance[0] = [0, 0]
    # distance[0] = [0, -1] # case where we set source node parent as -1

    adj = create_adj_matrix(edges, n)
    # adj = edges

    pq = [[0, 0]]

    heapq.heapify(pq)

    while len(pq):

        weight, source_node = heapq.heappop(pq)

        for node, weight in adj[source_node]:
            if distance[node][0] > distance[source_node][0] + weight:
                distance[node][0] = distance[source_node][0] + weight
                distance[node][1] = source_node
                heapq.heappush(pq, [distance[node][0], node])

    if distance[n - 1][1] == n - 1:
        return [-1]  # in case destination node n was not reached
    """
    # this also works incase we store default wait as inf
    shortest_path = [n - 1]
    print(distance)
    parent = distance[-1][1]

    while parent != 0:
        shortest_path.append(parent)
        parent = distance[parent][1]

    shortest_path.append(0)
    
    """
    shortest_path = []
    print(distance)
    node = n - 1
    while distance[node][1] != node:
        shortest_path.append(node)
        node = distance[node][1]

    shortest_path.append(0)

    return shortest_path[::-1]


edges = [[0, 1, 2], [1, 4, 5], [1, 2, 4], [0, 3, 1], [3, 2, 3], [2, 4, 1]]
n = 5
m = 6
print(dijkstras_algo(edges, n, m))
