"""
The closest to origin are the points whose distance is smallest from origin
distance formula = (sqrt[(x2-x1)^2 + (y2-y1)^2])

The smaller the distance the closer the point, hence MAX heap
since we need to keep key as distance , and that is relative we can just
store [(x2-x1)^2 + (y2-y1)^2] and avoid sqrt
also x1 and y1 are (0,0) , hence formula is x^2 + y^2
"""
import heapq
from typing import List


def origin_distance(x, y):
    # to calculate x^2 + y^2
    distance = x ** 2 + y ** 2
    return distance


def k_closest_origin(arr: List[List[int]], k):
    # to store the heap
    pq = []
    # iterate over the list of origins
    for i in arr:
        # calculate the distance of point from origin
        distance = origin_distance(i[0], i[1])
        # push to max heap, where key is the distance and
        # value is the origin pair
        heapq.heappush(pq, [-distance, i])

        # pop items if the len of heap is greater than k
        if len(pq) > k:
            heapq.heappop(pq)

    # get the values from the heap which are the closest to origin
    for i in range(len(pq)):
        pq[i] = pq[i][1]

    return pq


arr = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
print(k_closest_origin(arr, k))
