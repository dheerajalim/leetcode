"""
Problem Statement: You will be given an m x n grid, where each cell has the following values :

2  –  represents a rotten orange
1  –  represents a Fresh orange
0  –  represents an Empty Cell
Every minute, if a Fresh Orange is adjacent to a Rotten Orange in 4-direction ( upward, downwards, right, and left ) it becomes Rotten.

Return the minimum number of minutes required such that none of the cells has a Fresh Orange. If it’s not possible, return -1.
"""
from collections import deque


def rotten_oranges(grid):
    dq = deque()
    total_count = 0
    # 1. get count of the fresh and rotten oranges
    # 2. Insert all the rotten oranges to the queue

    row, col = len(grid), len(grid[0])

    # iterate through each element in grid
    # get total orange count
    # adding rotten to queue
    for i in range(row):
        for j in range(col):
            if grid[i][j] != 0:
                total_count += 1
            if grid[i][j] == 2:
                # adding the rotten orange to queue
                dq.append([i, j])

    # we need to check in all 4 directions
    # hence lets create a list
    # [x-1, x+1, y-1, y +1]
    row_update = [-1, 1, 0, 0]
    col_update = [0, 0, -1, 1]
    # to store rotten orange count
    rotten_count = 0
    # total time to rot all possible oranges
    total_time = 0

    # traverse through the queue and check for rotten oranges
    # until the queue is empty

    while dq:
        # since at same unit of time all the rotten oranges
        # will in parallel start rotting the nearby oranges
        # hence we take size of queue and rot all nearby oranges
        # in same unit of time
        size = len(dq)
        # the current size of queue is the oranges already rotten
        rotten_count += size
        for _ in range(size):
            # get the rotten orange from queue
            rotten_orange = dq.popleft()
            x, y = rotten_orange

            # check for the dinesion in all 4 directions
            for i in range(4):
                dx = x + row_update[i]
                dy = y + col_update[i]
                # if the dinesion is not valid or its empty or already rotten,
                # ignore that orange
                if dx < 0 or dx >= row or dy < 0 or dy >= col or grid[dx][dy] != 1:
                    continue
                # else rot that orange and add it to the queue
                else:
                    grid[dx][dy] = 2

                    # add the new rotten orange to queue
                    dq.append([dx, dy])

        # increment the time by 1
        # If we rot some oranges, then obviously our queue will not be empty
        # hence we put this ocndition
        if len(dq): total_time += 1

    # if the rotten count is equal to intial possible rotten count
    # then we were able to rot all oranges and return time
    if total_count == rotten_count:
        return total_time

    # else few oranges are still fresh and we return -1
    return -1


grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(rotten_oranges(grid))
