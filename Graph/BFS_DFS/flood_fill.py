"""
use BFS

https://leetcode.com/problems/flood-fill/submissions/1169535136/
"""

from collections import deque


def bfs(image, sr, sc, color, visited, rows, cols):
    dq = deque()
    # add the source to the queue
    dq.append([sr, sc])
    # mark it as visisted
    visited.add((sr, sc))

    # maintain the base color of the pixel to compare later
    base_color = image[sr][sc]
    # directions we can move to perfron flood fill
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while dq:
        # take the item from queue
        src_row, src_col = dq.popleft()
        # update its color to new color
        image[src_row][src_col] = color
        # look for same base color in all 4 directions
        for x, y in directions:
            dx = src_row + x
            dy = src_col + y
            # if the r/c are out of bound or if cell is already visisted or its not base color
            # we skip
            if dx < 0 or dx >= rows or dy < 0 or dy >= cols or (dx, dy) in visited or image[dx][dy] != base_color:
                continue

            # else append the cell to queue abnd mark it as visisted
            else:
                dq.append([dx, dy])
                visited.add((dx, dy))


def flood_fill(image, sr, sc, color):
    visited = set()
    rows, cols = len(image), len(image[0])

    # if the source is already of required color
    # we will not make cny change( leetcode example scenario)
    if image[sr][sc] == color:
        return image
    # else we call bfs on the source pixel
    bfs(image, sr, sc, color, visited, rows, cols)

    return image


image = [[0, 0, 0], [0, 0, 0]]
sr = 0
sc = 0
color = 0

print(flood_fill(image, sr, sc, color))
