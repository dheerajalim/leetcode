"""
Uses the concept of connected component counts

"""

from collections import deque


def bfs(row, col, visited, total_rows, total_cols, grid):
    # creating a queue (BFS requirement)
    dq = deque()

    # adding the source land to queue and visisted
    dq.append([row, col])
    visited.add((row, col))

    # possible directions to find land
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while dq:
        land_row, land_col = dq.popleft()

        # need to check in all vertical and horizontal directions
        for dr, dc in directions:
            d_row = land_row + dr
            d_col = land_col + dc

            # if the row/col is out of grid or is not 1 or is already visisted
            # skip that item
            if d_row < 0 or d_row >= total_rows or d_col < 0 or d_col >= total_cols \
                    or grid[d_row][d_col] != "1" or (d_row, d_col) in visited:
                continue
            # else add it to queue as it is visited
            else:
                dq.append([d_row, d_col])
                visited.add((d_row, d_col))


def number_of_islands(grid):
    # since we need to find the next land area
    # we can use BFS

    # to store the total island that are present
    islands = 0

    # if the element is grid is already visisted
    visited = set()
    row, col = len(grid), len(grid[0])

    # iterate through each grid item
    for r in range(row):
        for c in range(col):
            # if the item is 1 and is not visited, consider that as source
            # for the bfs
            if grid[r][c] == "1" and (r, c) not in visited:
                # similar concept to connected component bfs
                islands += 1
                bfs(r, c, visited, row, col, grid)

    return islands


grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
        ]

print(number_of_islands(grid))
