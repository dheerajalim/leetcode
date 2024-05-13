"""
https://leetcode.com/problems/largest-local-values-in-a-matrix/description/?envType=daily-question&envId=2024-05-12
"""


def largest_local(grid):
    n = len(grid)

    # create a result matrix of size n-2 * n-2
    result = [[0 for i in range(n - 2)] for _ in range(n - 2)]

    # get all the 8 directions to look for max value
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

    # now fill for each position in the result matrix
    for row in range(n - 2):
        for col in range(n - 2):
            # the starting point in grid matrix is i + 1 and j + 1
            x, y = row + 1, col + 1
            # initialize the max value with the starting point
            max_value = grid[x][y]
            # look in all 8 directions to get the maximum
            for p, q in directions:
                dx = p + x
                dy = q + y
                max_value = max(max_value, grid[dx][dy])

            result[row][col] = max_value

    return result


grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
# grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
print(largest_local(grid))
