"""
https://leetcode.com/problems/relative-ranks/description/?envType=daily-question&envId=2024-05-08
"""

import heapq


def find_relative_ranks(score):
    # heapify the score

    pq = []
    for j, i in enumerate(score):
        # max heap
        heapq.heappush(pq, (-i, j))

    # defaulting the rank to 1
    rank = 1
    heap_score = ""
    # iterate until the heap is emtpy
    while pq:
        # the first item will be the largest score when popped from heap
        _, index = heapq.heappop(pq)

        # we will check if the rank value is <= 3, then we need to add the gold, silver, bronze ranks
        if rank <= 3:

            if rank == 1:
                heap_score = "Gold Medal"
            elif rank == 2:
                heap_score = "Silver Medal"
            elif rank == 3:
                heap_score = "Bronze Medal"

            score[index] = heap_score
        # else we just add the score position as the value in the result
        else:
            score[index] = str(rank)

        rank += 1

    return score


score = [10, 3, 8, 9, 4]
score = [5, 4, 3, 2, 1]
print(find_relative_ranks(score))
