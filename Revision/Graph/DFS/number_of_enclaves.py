"""
https://leetcode.com/problems/number-of-enclaves/description/
"""

def dfs(board, i, j, count):
    board[i][j] = 0
    count[0] += 1
    dimensions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for x, y in dimensions:
        dx = i + x
        dy = j + y

        if dx < 0 or dx >= len(board) or dy < 0 or dy >= len(board[0]) or board[dx][dy] != 1:
            continue

        dfs(board, dx, dy, count)


def number_enclaves(grid):

    rows, cols = len(grid), len(grid[0])
    ones_count = 0
    converted_ones = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                ones_count += 1

    for i in range(rows):
        for j in range(cols):

            if i not in [0, rows - 1] and j not in [0, cols - 1]:
                continue

            if grid[i][j] == 1:
                count = [0]
                dfs(grid, i, j, count)
                converted_ones += count[0]

    return ones_count- converted_ones


grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
print(number_enclaves(grid))