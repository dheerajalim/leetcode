"""
idea is :
Use Dijakstra to reach from source 0,0 to r-1,c-1

the question requires you to fing the max effort from each path
and then retrun the min of these efforts

hence when we use dijkstra, we carry the max effort to the next node
the new_effort will always be max of (prev max effort, new_effort)

once we know that , and the new_effort is less than the current effort of that node
then we update it with the new_effort

that is , keep on carrying the max effort to next node and if that node has greater effort
 update it with smaler effort


"""

import heapq


def min_effort_path(heights):
    # the heights is a row * col grid
    row, col = len(heights), len(heights[0])

    # maintain a effort matrix to store the effort
    effort = [[float('inf') for _ in range(col)] for _ in range(row)]

    # effort for the starting point is marked as 0
    effort[0][0] = 0

    # directions to move
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # now we need to applu dijkstra to find the route with min effort
    # create a min heap with the source as 0,0

    pq = [[0, 0, 0]]

    heapq.heapify(pq)

    # iterate until we reach the end node or heap is complete

    while len(pq):
        current_effort, current_x, current_y = heapq.heappop(pq)
        # this means that we have reached the destination node
        # and the min effort to reach here is already computed
        if current_x == row - 1 and current_y == col - 1:
            return current_effort

        for x, y in directions:
            dx = current_x + x
            dy = current_y + y

            if dx < 0 or dx >= row or dy < 0 or dy >= col:
                continue

            # the new node will always take the max effort of the current path
            new_effort = max(current_effort, abs(heights[current_x][current_y] - heights[dx][dy]))
            # if the new effort is lesser that the max effort computed for that node
            # this means that we have another path which if takes max effort on its
            # path reaches this node is less effort, hence we update the effort of
            # the node with smaller effort value
            if new_effort < effort[dx][dy]:
                effort[dx][dy] = new_effort
                heapq.heappush(pq, [new_effort, dx, dy])

    return effort


heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
heights = [[1, 10, 6, 7, 9, 10, 4, 9]]
print(min_effort_path(heights))
