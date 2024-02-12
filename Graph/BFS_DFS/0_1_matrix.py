"""
https://leetcode.com/problems/01-matrix/description/

Need to return the distance to nearest 0,

the idea is if we need to find distance from 1 to 0
then distance from 0 to 1 will also be same
hence we start from all the 0 position and reach their nearest 1's
"""

from collections import deque


def nearest_zeros(matrix):
    # create a new distance matrix
    # with all 0's as 0 and every other cell as -1
    # since distance of 0 from 0 is 0

    rows, cols = len(matrix), len(matrix[0])

    distance_matrix = [[-1 for _ in range(cols)] for _ in range(rows)]

    # create a queue to store the 0 position
    # these will be our starting point

    dq = deque()

    # to move in 4 directions from cell
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for i in range(rows):
        for j in range(cols):
            # if the matrix has 0, we update distance matrix with 0
            if matrix[i][j] == 0:
                distance_matrix[i][j] = 0
                dq.append([i, j])
    while dq:
        r, c = dq.popleft()

        for x, y in directions:
            dx = r + x
            dy = c + y
            # if the cell in all 4 directions is not in range and is not -1 , then we continue
            if dx < 0 or dx >= rows or dy < 0 or dy >= cols or distance_matrix[dx][dy] != -1:
                continue
            # else we update it to current cell + 1 and add it to queue
            else:
                distance_matrix[dx][dy] = distance_matrix[r][c] + 1
                dq.append([dx, dy])

    return distance_matrix


mat = [[0, -1, -1], [-1, -1, -1], [-1, -1, -1]]
mat = [[0], [0], [0], [0], [0]]

print(nearest_zeros(mat))
