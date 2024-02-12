"""
https://leetcode.com/problems/number-of-enclaves/description/
"""
from collections import deque


def num_of_enclaves(grid):
    # traverse through all the cells in border
    # add the 1's coordinates to the queue

    # store the total number of 1's
    total_land_count = 0

    rows, cols = len(grid), len(grid[0])

    dq = deque()
    # to maintain the cell which can reach boundary
    reachable_count = 0
    # traverse through all the cell in grid
    for r in range(rows):
        for c in range(cols):
            # check for all the land cells
            if grid[r][c] == 1:
                # increment total land count
                total_land_count += 1
                # if the land is boundary, add to the queue
                # also mark them as visisted by changing it to "True"
                # update reachable_count += 1 as these land an reach boundary
                if r in [0, rows - 1] or c in [0, cols - 1]:
                    dq.append([r, c])
                    grid[r][c] = "True"
                    reachable_count += 1

    # all possible 4 directions
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while dq:
        r, c = dq.popleft()

        for x, y in directions:
            dx = r + x
            dy = c + y
            # if the cell is not land and is out of valid row/col or is already visited
            # we ignore this cell
            if dx < 0 or dx >= rows or dy < 0 or dy >= cols or grid[dx][dy] != 1 or grid[dx][dy] == "True":
                continue
            # else mark it as visited
            # add it to the queue and increment the reachable count by 1
            else:
                grid[dx][dy] = "True"
                dq.append([dx, dy])
                reachable_count += 1

    # return the difference of total land and land that can reach boundary
    # this gives land that cannot reach boundary
    return total_land_count - reachable_count


grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
grid = [[1, 1, 1, 1], [0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
print(num_of_enclaves(grid))
