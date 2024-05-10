"""
https://leetcode.com/problems/maximize-happiness-of-selected-children/description/?envType=daily-question&envId=2024-05-09
"""

import heapq


def max_happiness_sum(happiness, k):
    # max heapify
    pq = []
    for i in happiness:
        heapq.heappush(pq, -i)

    max_happy_sum = 0

    for j in range(0, k):
        # the child with max happiness
        child_happiness = -1 * heapq.heappop(pq)

        # if the child_happiness , its position is <= 0, then we add 0
        # as we cannot go beyond 0
        if child_happiness - j <= 0:
            max_happy_sum += 0
        # else we just add the child_happiness - its position in max heap
        else:
            max_happy_sum += child_happiness - j

    return max_happy_sum


happiness = [2, 3, 4, 5]
k = 1

print(max_happiness_sum(happiness, k))
