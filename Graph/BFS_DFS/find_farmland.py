"""
https://leetcode.com/problems/find-all-groups-of-farmland/description/?envType=daily-question&envId=2024-04-20
"""

from collections import deque


def bfs(land, i, j, visited):
    visited.add((i, j))
    dq = deque()
    dq.append([i, j])

    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while dq:
        i, j = dq.popleft()
        for x, y in directions:
            dx = x + i
            dy = y + j

            if dx < 0 or dx >= len(land) or dy < 0 or dy >= len(land[0]) or (dx, dy) in visited or land[dx][dy] == 0:
                continue

            visited.add((dx, dy))
            dq.append([dx, dy])

    # once the farmland is found, we actually will be at the last part of the farmland
    # and i, j will be the coordinates of this piece of land, so we return those coordinates
    return i, j


def find_farmland(land):
    visited = set()
    result = []
    for i in range(len(land)):
        for j in range(len(land[0])):
            # to store the coordinates of the farmland
            temp_result = []
            # start from the farmland i.e. cell value == 1
            if land[i][j] == 1 and (i, j) not in visited:
                # we first store the coordinates of the starting point of the farmland
                temp_result.extend([i, j])
                bottom_corner_i, bottom_corner_j = bfs(land, i, j, visited)
                # now we add the bottom last farmland to the temp_result
                temp_result.extend([bottom_corner_i, bottom_corner_j])

                # after every iteration we store the answer in the result list
                result.append(temp_result)

    return result


land = [[1, 0, 0], [0, 1, 1], [0, 1, 1]]

print(find_farmland(land))
