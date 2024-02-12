"""
Difference is that we see the diagonal direction as well
"""

from collections import deque


def bfs(grid, r, c, rows, cols, visited):
    dq = deque()
    dq.append([r, c])
    visited[r][c] = True

    # directions
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1],
    [-1, -1], [-1, 1], [1, -1], [1, 1]
                  ]

    while dq:

        island_x, island_y = dq.popleft()

        for x, y in directions:
            dx = island_x + x
            dy = island_y + y

            if dx < 0 or dx >= rows or dy < 0 or dy >= cols or grid[dx][dy] != 1 or visited[dx][dy] is True:
                continue
            else:
                dq.append([dx, dy])
                visited[dx][dy] = True


def number_of_islands(grid):
    rows, cols = len(grid), len(grid[0])

    visited = [[False for _ in range(cols)] for _ in range(rows)]

    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and visited[r][c] is False:
                islands += 1
                bfs(grid, r, c, rows, cols, visited)

    return islands

grid = [[0,1], [1,0], [1,1], [1,0]]
grid = [[0,1,1,1,0,0,0], [0,0,1,1,0,1,0]]

print(number_of_islands(grid))
