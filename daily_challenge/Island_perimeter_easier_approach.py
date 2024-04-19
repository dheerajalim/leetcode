"""
https://leetcode.com/problems/island-perimeter/?envType=daily-question&envId=2024-04-18
"""


def dfs(grid, i, j, perimeter):
    grid[i][j] = -1
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for x, y in direction:
        dx = x + i
        dy = y + j

        # whenever we are crossing boundary or reaching water, that means land's border
        # is counted in perimeter
        if dx < 0 or dx >= len(grid) or dy < 0 or dy >= len(grid[0]) or grid[dx][dy] == 0:
            perimeter[0] += 1
            continue

        # in case a land is already visited, we continue
        if grid[dx][dy] == -1:
            continue

        dfs(grid, dx, dy, perimeter)


def island_perimeter(grid):
    perimeter = [0]
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if grid[i][j] == 1:
                dfs(grid, i, j, perimeter)
                return perimeter


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]

grid = [[1, 1], [1, 1]]

print(island_perimeter(grid))
`