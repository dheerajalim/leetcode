"""
https://leetcode.com/problems/max-area-of-island/description/

Connected components concept , in each component we will increment count + 1
whenever we pop from queue, this will give us the count of 1's
"""

from collections import deque


def bfs(grid, visited, i, j):
    dq = deque()
    dq.append([i, j])
    visited[i][j] = True

    dimensions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    count = 0
    while dq:

        p, q = dq.popleft()
        count += 1
        for x, y in dimensions:
            dx = p + x
            dy = q + y

            if dx < 0 or dx >= len(grid) or dy < 0 or dy >= len(grid[0]) or visited[dx][dy] is True or grid[dx][
                dy] != 1:
                continue

            visited[dx][dy] = True
            dq.append([dx, dy])

    return count


def max_area_island(grid):
    rows, cols = len(grid), len(grid[0])

    visited = [[False for _ in range(cols)] for _ in range(rows)]

    max_area = 0

    for i in range(rows):
        for j in range(cols):

            if visited[i][j] is False and grid[i][j] == 1:
                area = bfs(grid, visited, i, j)
                max_area = max(max_area, area)

    return max_area


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

print(max_area_island(grid))