"""

1. Use Bricks wherever possible else use ladder
2. Maintain a max heap with the number of bricks used
3. If total height diff is less than total bricks and a ladder is available to replace prev brick used gap ,
    then from PQ pop the max bricks and reduce the ladder count by 1
    Use the required bricks and update the PQ and the total bricks that we have now
4. Return once we cannot move further with 0 bricks and unusable or 0 bricks

"""

import heapq


def furthest_building(heights, bricks, ladders):
    pq = []
    count = 0

    for i in range(0, len(heights) - 1):

        if heights[i] >= heights[i + 1]:
            count += 1

        elif heights[i] < heights[i + 1]:

            height_diff = heights[i + 1] - heights[i]

            if height_diff <= bricks:
                bricks -= height_diff
                heapq.heappush(pq, -height_diff)
                count += 1

            # as we can never reach by even using al bricks
            # hence use ladder

            elif ladders:

                if pq and -pq[0] > height_diff:
                    bricks = (-heapq.heappop(pq) + bricks) - height_diff
                    ladders -= 1
                    count += 1
                    heapq.heappush(pq, -height_diff)

                else:
                    ladders -= 1
                    count += 1

            else:
                return count

    return count


heights = [9,15,19,24,27,29]
bricks = 10
ladders = 2

print(furthest_building(heights, bricks,ladders))

