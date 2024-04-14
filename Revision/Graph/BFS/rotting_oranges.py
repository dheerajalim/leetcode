"""
0 : empty , 1 : fresh, 2 : rotten
"""

from collections import deque


def rotting_oranges(grid):
    dq = deque()
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    total_count, rotten_count = 0, 0
    # iterate and get all the rotten oranges and total count and rotten count
    # store the position of the rotten oranges
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if grid[i][j] == 2:
                rotten_count += 1
                visited[i][j] = True
                dq.append([i, j])

            if grid[i][j] != 0:
                total_count += 1

    # apply BFS to this queue and check how many nearby fresh oranges can be rotten

    dimensions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    total_time = 0
    while dq:

        size = len(dq)

        for _ in range(size):

            p, q = dq.popleft()

            for x, y in dimensions:
                dx = p + x
                dy = q + y

                if dx < 0 or dx >= len(grid) or dy < 0 or dy >= len(grid[0]) or visited[dx][dy] is True or grid[dx][
                    dy] != 1:
                    continue

                visited[dx][dy] = True
                grid[dx][dy] = 2
                rotten_count += 1
                dq.append([dx, dy])

        if len(dq):
            total_time += 1

    return total_time if rotten_count == total_count else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
print(rotting_oranges(grid))
