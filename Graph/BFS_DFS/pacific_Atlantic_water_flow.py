def dfs(heights, ocean, r, c, rows, cols):

    ocean.add((r, c))

    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for x, y in directions:
        dx = x + r
        dy = y + c

        if dx < 0 or dx >= rows or dy < 0 or dy >= cols or (dx,dy) in ocean or heights[dx][dy] < heights[r][c]:
            continue

        dfs(heights, ocean, dx, dy, rows, cols)


def pacific_atlantic(heights):
    pac, atl = set(), set()

    rows, cols = len(heights), len(heights[0])
    for c in range(cols):
        dfs(heights, pac, 0, c, rows, cols)
        dfs(heights, atl, rows - 1, c, rows, cols)

    for r in range(rows):
        dfs(heights, pac, r, 0, rows, cols)
        dfs(heights, atl, r, cols - 1, rows, cols)

    result = []
    for r in range(rows):
        for c in range(cols):
            if (r,c) in pac and (r,c) in atl:
                result.append([r,c])

    print(result)

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
pacific_atlantic(heights)