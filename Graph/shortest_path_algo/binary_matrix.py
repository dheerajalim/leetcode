"""

Idea is to prefer
 1. diagonal first
 2. then the next row
 3. then the same row next
 4. then the previous non visisted

 But then , i realised that when the edge distance is 1, then bfs always finds the shortest distance
"""

# [[0,0,0],[1,1,0],[1,1,0]]

from collections import deque


def bfs(grid, distance, visited):

    n = len(grid)
    visited[0][0] = True
    dq = deque()
    # add the first node (source) with its x,y, and distance
    # the distance of first node is 1 , as we need to consider it as well
    # in the shortest path length
    dq.append([0, 0, 1])

    # all possible 8 directions
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1],
                  [1, -1], [1, 0], [1, 1]
                  ]

    while dq:
        curr_x, curr_y, curr_distance = dq.popleft()
        for x, y in directions:
            dx = curr_x + x
            dy = curr_y + y
            # if the node is out of boundary or not  0 or already visited, then we ignore
            if dx < 0 or dx >= n or dy < 0 or dy >= n or grid[dx][dy] != 0 or visited[dx][dy] is True:
                continue

            # update the distance of the node from the source
            distance[dx][dy] = curr_distance + 1
            dq.append([dx, dy, distance[dx][dy]])
            visited[dx][dy] = True


def binary_matrix(grid):
    n = len(grid)
    # check the edge cases
    # if there is only one item and it is 0
    if len(grid) == 1 and grid[0][0] == 0:
        return 1
    # if the first node is not 0
    if grid[0][0] != 0:
        return -1
    # if the last node is not 0
    if grid[n - 1][n - 1] != 0:
        return -1

    # to maintain the visited node and the distance of each node
    visited = [[False for _ in range(n)] for _ in range(n)]
    distance = [[-1 for _ in range(n)] for _ in range(n)]

    # call bfs
    bfs(grid, distance, visited)

    return distance[-1][-1]


grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
grid = [[0, 1], [1, 0]]
grid = [[0]]
print(binary_matrix(grid))
