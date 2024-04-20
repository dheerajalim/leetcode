"""
https://leetcode.com/problems/number-of-islands/description/?envType=daily-question&envId=2024-04-19
"""


def dfs(grid, i, j, visited):
    visited[i][j] = True

    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for x, y in directions:
        dx = i + x
        dy = y + j

        if dx < 0 or dx >= len(grid) or dy < 0 or dy >= len(grid[0]) or visited[dx][dy] is True or grid[dx][dy] == "0":
            continue

        visited[dx][dy] = True
        dfs(grid, dx, dy, visited)


def number_islands(grid):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if visited[i][j] is False and grid[i][j] == "1":
                count += 1
                dfs(grid, i, j, visited)

    return count


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(number_islands(grid))
