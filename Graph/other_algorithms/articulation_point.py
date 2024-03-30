"""

yhe similar hai bridges wali problem ke,

Similarities:
1. if adj node is parent, then continue


just difference are below
1. if the adjacent node is visited, then take the min (low_time[src], time_in[node])
2. if the adjacent ode is not visisted: then call the dfs on it
    > then check low_time[src] = min(low_time[src], low_time[node])
    > if low_time[node] >= low_time[src] # here >= and not >
        then this node is the articulation point

Also note that same articulation point can be from different path
hence we maintian a set

Root ka hisab alag hai, kyunki root tabhi articulation point hga
jab uske atleast 2 child ho

"""


def create_adj_list(n, edges):
    adj_list = [[] for _ in range(n)]

    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    return adj_list


def dfs(adj, src, parent, time_in, low_time, visited, points, time):
    visited[src] = True
    time_in[src] = time[0]
    low_time[src] = time[0]

    time[0] += 1
    child = 0
    for node in adj[src]:

        # if the node is parent node, then no action needs to be done
        # as we do not update time for parent from who we came
        # this will not make any sense
        if node == parent:
            continue

        # if we reach an already visited node, this means
        # that we were able to already reach it, we will just update
        # its low time as there is a possible parent that reached this node
        # since here we are checking a node we use time_in of visited node
        # contrary to low_time in bridges
        if visited[node]:
            low_time[src] = min(time_in[node], low_time[src])

        # this node is not yet visited
        elif visited[node] is False:

            dfs(adj, node, src, time_in, low_time, visited, points, time)

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
            # compared to src node time_in, this means that there exists a articulation point here
            # Why? because the node can never be reached by its src node if we remove this node
            # because the node low_time is higher or equal to  which means src and node does not have a
            # common parent or if they have its the src node only
            if low_time[node] >= time_in[src] and parent != -1:
                points.add(src)

            # to calculate the child node of each node
            child += 1

    # if the child is > 1 and its root node, then we add it to articulate points
    if child > 1 and parent == -1:
        points.add(src)


def articulation_point(n, edges):
    visited = [False] * n
    time_in = [0] * n
    low_time = [0] * n

    time = [0]

    points = set()

    adj_list = create_adj_list(n, edges)
    for i in range(n):
        if visited[i] is False:
            dfs(adj_list, i, -1, time_in, low_time, visited, points, time)

    return -1 if len(points) == 0 else sorted(list(points))


edges = [[0, 1], [0, 2], [0, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]]
n = 7
print(articulation_point(n, edges))
