"""
https://leetcode.com/problems/number-of-provinces/description/

Given is a matrix so we convert it into dj list
"""

from collections import deque


def matrix_to_list(matrix):
    adj_list = [[] for _ in range(len(matrix))]

    for i in range(len(matrix)):

        for j in range(len(matrix[0])):

            if i != j and matrix[i][j] == 1:
                adj_list[i].append(j)

    return adj_list


def bfs(adj_list, source, visited):
    dq = deque()

    # adding 0th in dex as the source
    dq.append(source)
    visited[source] = True

    while dq:

        source = dq.popleft()
        for vertex in adj_list[source]:
            if not visited[vertex]:
                visited[vertex] = True
                dq.append(vertex)


def find_provinces(is_connected):
    adj_list = matrix_to_list(is_connected)

    visited = [False] * len(adj_list)
    count = 0

    for i in range(len(adj_list)):
        if visited[i] is False:
            bfs(adj_list, i, visited)
            count += 1

    return count


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(find_provinces(isConnected))
