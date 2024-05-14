"""
https://leetcode.com/problems/path-with-maximum-gold/description/?envType=daily-question&envId=2024-05-14

We will start the backtracking by starting from a non zero item
"""


def backtracking(grid, i, j, curr, result):
    # base condition : if position is out of bound or has no gold, return False
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
        return False

    # we add the current position gold
    curr[0] += grid[i][j]

    # we also stor the current position gold, so that after backtracking we can undo the visited grid
    temp = grid[i][j]
    # this is done to mark the position as visited
    grid[i][j] = 0
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for x, y in directions:
        dx = i + x
        dy = j + y
        # backtracking to find a path with gold mines
        backtracking(grid, dx, dy, curr, result)

    # once we have discovered a path, we just store the gold we collected
    # and compare ot with the max gold we collected from any other path
    result[0] = max(result[0], curr[0])

    # also we subtract the current position value ,as we have now backtracked from that position
    curr[0] -= temp
    # undo the visited position by placing the original value back
    grid[i][j] = temp


def get_max_gold(grid):
    """
    We start exploring from all possible position in the grid
    and check for the max gold value

    """
    m, n = len(grid), len(grid[0])

    max_result = 0
    result = [0]
    curr = [0]
    # we start iterating the non-zero grid item, which is the position that has gold
    for i in range(m):
        for j in range(n):

            if grid[i][j] != 0:
                backtracking(grid, i, j, curr, result)
                max_result = max(max_result, result[0])

    return max_result


grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]

print(get_max_gold(grid))
