"""
https://leetcode.com/problems/word-search/description/
"""


def find(word, board, x, y, n, m, idx):
    # the directions to move in
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    # if the word len and the id (word index) match then
    # the word is found
    if idx == len(word):
        return True

    # if the index is out of  bound or is already visited
    # then we return False
    if x < 0 or x >= n or y < 0 or y >= m or board[x][y] == "$":
        return False

    # of the character of word and board char position do not match
    # return False
    if board[x][y] != word[idx]:
        return False

    # we store the actual value of the position in board
    # this helps to restore original value during backtrack
    temp = board[x][y]
    # mark the value as visited
    board[x][y] = "$"

    # move i n all 4 possible directions
    for dx, dy in directions:
        pos_x = x + dx
        pos_y = y + dy

        # call the find function recursively for the new cell position
        # if the function return True, then we found the word
        if find(word, board, pos_x, pos_y, n, m, idx + 1):
            return True

    # if the word is not found, we backtrack
    # and update the board with original value
    board[x][y] = temp

    return False


def exists(board, word):
    n = len(board)  # row
    m = len(board[0])  # col

    # iterate over the word
    for i in range(n):
        for j in range(m):
            # if the first character of the word matches the board
            # then we start the finding of the word
            if board[i][j] == word[0]:
                # if a word is found, return True else return False
                if find(word, board, i, j, n, m, 0):
                    return True

    return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

print(exists(board, word))
