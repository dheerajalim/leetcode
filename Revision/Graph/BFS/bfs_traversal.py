# this will give input as adj list


from collections import deque


def bfs(adj_list, source):
    n = len(adj_list)

    visited = [False] * n

    dq = deque()

    # adding 0th in dex as the source
    dq.append(source)
    visited[source] = True

    while dq:

        source = dq.popleft()
        print(source, end=" ")
        for vertex in adj_list[source]:
            if not visited[vertex]:
                visited[vertex] = True
                dq.append(vertex)


adj = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4], [2, 3]]
# we start with 0th node as source
source = 0

bfs(adj, source)