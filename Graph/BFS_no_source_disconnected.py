"""
BFS for a graph which is disconnected and
has no source input
In that case we will call the BFS traversal for each verted and maintain
a visited list for the vertices as well

Time Complexity : O(V + E) , Runs V times for all source vertex
                            E for each vertex
"""

from collections import deque


def bfs(adj, source, visited):
    dq = deque()

    dq.append(source)
    visited[source] = True

    while dq:

        source = dq.popleft()
        print(source, end=" ")
        for vertex in adj[source]:
            if visited[vertex] is False:
                dq.append(vertex)
                visited[vertex] = True


def bfs_disconnected(adj):
    # this is similar to BFS alog
    # the difference here is that we iterate
    # over all the vertices and call BFS for
    # each vertex which is not visited yet

    visited = [False] * len(adj)
