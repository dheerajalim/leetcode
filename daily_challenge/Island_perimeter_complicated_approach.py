"""
https://leetcode.com/problems/island-perimeter/?envType=daily-question&envId=2024-04-18
"""

"""
1. We change all land value to 4, as max possible perimeter value is 4
2. Then apply DFS from the first land we reach and update its visited_from
3. We add 'to' node details in from node and from node details in 'to', to identify that a border is shared
4. And keep on decrementing the perimeter value 
"""


def update_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # update the grid cell value to 4 for all lands
            # as we assume that maximum perimeter a call can have is 4
            if grid[i][j] == 1:
                grid[i][j] = 4


def dfs(grid, visited_from, i, j):
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for x, y in direction:
        dx = x + i
        dy = y + j

        if dx < 0 or dx >= len(grid) or dy < 0 or dy >= len(grid[0]) or (dx, dy) in visited_from[i][j] or grid[dx][
            dy] == 0:
            continue
        # we reduce the perimeter for the from and to both land cells
        # as now they have a common border, which will not be part of perimeter
        grid[i][j] -= 1
        visited_from[i][j].append((dx, dy))
        grid[dx][dy] -= 1
        visited_from[dx][dy].append((i, j))

        dfs(grid, visited_from, dx, dy)


def island_perimeter(grid):
    # update the grid cell value to 4 for all the lands
    update_grid(grid)
    # visited_from store the list of dimension for the to and from land
    # example if I can move from [0,1] to [1,1], then both the grids
    # will update the visited_from
    visited_from = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if grid[i][j] == 4:
                dfs(grid, visited_from, i, j)
                break

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            perimeter += grid[i][j]

    return perimeter


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]

grid = [[1, 1], [1, 1]]

print(island_perimeter(grid))
