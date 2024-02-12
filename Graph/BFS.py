"""
Uses Level Order traversal Loginc
The difference here is that we maintain visited list
to check if the vertex is already visisted
"""

from collections import deque


def bfs(ajd, source):
    """

    :param ajd: adjacency list
    :param s: SOURCE vertex
    :return: Print the BFS traversal
    """

    dq = deque()
    # to mark if the vertex is visited
    visited = [False] * len(ajd)

    # add the source to the queue
    dq.append(source)
    # mark that the source is visited
    visited[source] = True

    # iterate through the queue
    while dq:

        # get the top of the queue
        source = dq.popleft()
        # print it as BFS traversal
        print(source, end=" ")

        # for all the vertex from the source
        # add them to the queue
        for vertex in ajd[source]:
            # if the vertex from current source
            # is not visited , mark it as visited and add to queue
            if visited[vertex] is False:
                dq.append(vertex)
                visited[vertex] = True


adj = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4], [2, 3]]
source = 0

bfs(adj, source)
