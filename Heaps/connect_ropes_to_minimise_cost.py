"""
There are given N ropes of different lengths, we need to connect these ropes into one rope. The cost to connect two ropes is equal to sum of their lengths.
The task is to connect the ropes with minimum cost. Given N size array arr[] contains the lengths of the ropes.

Example 1:

Input:
n = 4
arr[] = {4, 3, 2, 6}
Output:
29
"""

import heapq


def connect_ropes(arr):
    total_cost = 0
    pq = arr
    # create a min heap
    heapq.heapify(pq)

    # iterate until we have at least 2 elements in the heap
    while len(pq) >= 2:
        # pop the first min element
        min_rope_1 = heapq.heappop(pq)
        # pop the secon min element
        min_rope_2 = heapq.heappop(pq)
        # the current cost is the sum of two min elements
        cost = min_rope_1 + min_rope_2
        # keep on updating the total cost
        total_cost += cost
        # add the current cost to the min heap
        heapq.heappush(pq, cost)

    return total_cost


arr = [1, 4, 3, 5, 2]
arr = [4, 3, 2, 6]

print(connect_ropes(arr))
