"""
https://leetcode.com/problems/surrounded-regions/description/
"""


# 1. Go through border and find "O" if exists convert it to T and run DFS over it surrounding
# 2. Run through each grid cell and convert "O" to "X"
# 3. Run through each grid cell and reconvert "T" to "O"


def update_border(r, c, rows, cols, board):
    # directions to check in all 4 cells
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # base case, if the row/col are outside board or are not "O"
    # then return
    if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
        return

    # set the border "O" to "T" to avoid capturing border items
    board[r][c] = "T"

    # now run DFS on all the possible directions that needs updation
    for dr, dc in directions:
        d_row = r + dr
        d_col = c + dc
        update_border(d_row, d_col, rows, cols, board)



def capture_surrounding(board):
    # taking total rows and cols
    rows, cols = len(board), len(board[0])

    # run through the board
    for r in range(rows):
        for c in range(cols):
            # checking if the row and col are of the border and are "o"
            # if yes then call the update border function
            if board[r][c] == "O" and ((r == 0 or r == rows - 1) or (c == 0 or c == cols - 1)):
                update_border(r, c, rows, cols, board)

    # run through each cell of the board and convert "O" to "X"
    # this marks capturing of the "O", note that border "O"
    # are already converted to T and using DFS
    # all related O are converted to T

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "T":
                board[r][c] = "O"

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","O","X"]]

capture_surrounding(board)

print(board)
