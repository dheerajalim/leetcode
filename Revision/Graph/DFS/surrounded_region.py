"""
https://leetcode.com/problems/surrounded-regions/


The idea is to use DFS from the borders and convert all the O that we can reach to T
because a O on border is useless as it cannot be covered by water from all 4 sides
hence if this can reach other ) then that is also useless

Matkab border wale sare O untouchable hai, kyunkiwo kabi b water se 4 direction
me surround nai ho sakte and yhe untouchable kisi aur O ko touch krte hai to
wo b untouchable ho jyega

"""


def dfs(board, i, j):
    board[i][j] = "T"

    dimensions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for x, y in dimensions:
        dx = i + x
        dy = j + y

        if dx < 0 or dx >= len(board) or dy < 0 or dy >= len(board[0]) or board[dx][dy] != "O":
            continue

        dfs(board, dx, dy)


def surrounded_region(board):
    # no need to maintain visited as we are already changing O to T
    # which makes it mark as visited
    rows, cols = len(board), len(board[0])

    for i in range(rows):
        for j in range(cols):

            if i not in [0, rows - 1] and j not in [0, cols - 1]:
                continue

            if board[i][j] == "O":
                dfs(board, i, j)

    # iterate and change all T to O and everything else to X
    for i in range(rows):
        for j in range(cols):

            if board[i][j] == "T":
                board[i][j] = "O"
            else:
                board[i][j] = "X"

    print(board)


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

surrounded_region(board)
