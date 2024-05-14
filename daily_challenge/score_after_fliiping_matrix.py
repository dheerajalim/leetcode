"""
https://leetcode.com/problems/score-after-flipping-matrix/?envType=daily-question&envId=2024-05-13


The idea is to check if the column 0 for all rows is 1 or not.
This allows to maximize the row value, hence we flip the row if the first colum in each row is set to 0

After that we check column wise from column 1 (0 indexed), and see if the count of 0 > 1, then we flip the column as we
need to maximize the no. of 1's in each column
"""


def matrix_score(grid):
    m, n = len(grid), len(grid[0])

    # to store the count of 1's in each column
    hash_map = {}

    # traverse row wise and flip bits if the first bit is 0
    for i in range(m):
        if grid[i][0] == 0:
            for j in range(n):
                grid[i][j] = 1 - grid[i][j]

    # need to calculate column wise 1's
    for i in range(1, n):
        for j in range(m):
            # if the column at each row is 1, then increase it's count in that colum key in hash map
            if grid[j][i] == 1:
                if hash_map.get(i):
                    hash_map[i] += 1
                else:
                    hash_map[i] = 1

    # now we will go column wise , start from column 1 and start flipping
    # if the count of 0 > count of 1's in each column

    for i in range(1, n):
        # this condition means that if the column key in not present in hash map, that means that entire column had 0's
        # hence we flip all the bits in that column
        if not hash_map.get(i):
            for j in range(m):
                grid[j][i] = 1 - grid[j][i]  # this will always become 1

        # else we check if the key is present and its 0 count > 1 count,
        # so we flip the column
        elif hash_map.get(i) and m - hash_map[i] > hash_map[i]:
            # then we flip the column
            for j in range(m):
                grid[j][i] = 1 - grid[j][i]

    result = 0

    # then we convert each row to integer value and total the rows to get result
    for row in grid:
        result += int("".join(map(str, row)), 2)

    return result


grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
grid = [[0, 1, 1], [1, 1, 1], [0, 1, 0]]
print(matrix_score(grid))
