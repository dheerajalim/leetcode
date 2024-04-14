"""https://leetcode.com/problems/number-of-islands/description/"""

# concept of connected components

from collections import deque


def bfs(grid, visited, i, j):
    dq = deque()
    dq.append([i, j])
    visited[i][j] = True

    dimensions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while dq:

        p, q = dq.popleft()
        for x, y in dimensions:
            dx = p + x
            dy = q + y

            if dx < 0 or dx >= len(grid) or dy < 0 or dy >= len(grid[0]) or visited[dx][dy] is True or grid[dx][
                dy] != "1":
                continue

            visited[dx][dy] = True
            dq.append([dx, dy])


def num_islands(grid):
    rows, cols = len(grid), len(grid[0])

    visited = [[False for _ in range(cols)] for _ in range(rows)]

    island_count = 0

    for i in range(rows):
        for j in range(cols):

            if visited[i][j] is False and grid[i][j] == "1":
                bfs(grid, visited, i, j)
                island_count += 1

    return island_count


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(num_islands(grid))
