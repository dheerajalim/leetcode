"""

2 list maintain krenge : time and low time
DFS usek krke traverse krenge and time and low time update krenege as same as node example 0 node ka time =0
low time =0, 1 node ka time = 1 low time =1

Whenever, we reach at a node, jiske adjacent nodes visited han and uska low time , current node ke low se kam hai
and wo node parent node of current node nai hai tho hum current node ka low time = adjacent node ke low time kr denge


aur jab b adjacent node aur current node ka low time same hoga tab hum bridge man lenge
"""


def create_adj_list(n, edges):
    adj_list = [[] for _ in range(n)]

    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    return adj_list


def dfs(adj, src, parent, time_in, low_time, visited, bridge, time):
    # mark the src node as visisted
    visited[src] = True

    # increment the time_in and low_time
    time_in[src] = time[0]
    low_time[src] = time[0]
    time[0] += 1

    # traverse the adjacent nodes
    for node in adj[src]:

        # if the node is parent node, then no action needs to be done
        # as we do not update time for parent from who we came
        # this will not make any sense
        if node == parent:
            continue

        # if we reach an already visited node, this means
        # that we were able to already reach it, we will just update
        # its low time as there is a possible parent that reached this node
        if visited[node]:
            low_time[src] = min(low_time[node], low_time[src])

        # this node is not yet visited
        elif visited[node] is False:
            dfs(adj, node, src, time_in, low_time, visited, bridge, time)

            # the below steps are critical, to understand
            # as we backtrack to the node in DFS recursion
            # we check if the node we came from has lower time then current node
            # if yes we take its lower time as this ensures that there is some higher parent
            # which can reach both of us

            # Step 1 : We need to update the src node low time compared with
            # its adjacent node from which it is backtracking, this means that
            # both of them have a higher parent node that can reach
            # them even if we remove the edge
            low_time[src] = min(low_time[node], low_time[src])

            # step 2 : if the node from which we backtracked has higher low_time
            # compared to src node time_in, this means that there exists a bridge here
            # Why? because the node can never be reached by its src node if we break the connection
            # between them because the node low_time is higher which means src and node does not have a
            # common parent

            if low_time[node] > time_in[src]:
                bridge.append([src, node])


def bridges(n, edges):
    # convert edges to adj list
    adj_list = create_adj_list(n, edges)

    # now we need to do the DFS traversal and store the timein and lowtime
    time_in = [0] * n
    low_time = [0] * n

    # to mark the node as visited in DFS traversal
    visited = [False] * n

    # to store the bridges
    bridge = []

    # to update the time for each node
    time = [0]

    # we will start from the 0th node as source
    # since the problem will be single connected component
    # hence we don't need to pass all nodes to DFS

    dfs(adj_list, 0, -1, time_in, low_time, visited, bridge, time)

    print(bridge)


edges = [[0, 1], [0, 3], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [5, 8], [6, 7], [8, 7], [7, 9], [9, 10], [9, 11],
         [10, 11]]
n = 12
bridges(n, edges)
