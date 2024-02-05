"""
at any index i, the possible sorted value at k
will be present in range [i - k  , i + k] inclusive
"""

import heapq


def k_sorted(arr, k):
    # to store min heap
    pq = []
    # to store the sorted array
    result = []

    # iterate over the k sorted array
    for i in arr:
        # push the item into heap (min heap)
        heapq.heappush(pq, i)
        # if the length of the heap is grater than k
        # that means the top element of min heap is
        # the smallest in the k range
        if len(pq) > k:
            # pop the top element from min heap
            # append it to result array
            result.append(heapq.heappop(pq))

    # after the complete array traversal
    # keep on popping from heap until it is empty
    while len(pq) > 0:
        result.append(heapq.heappop(pq))
    # contains sorted array
    return result


arr = [6, 5, 3, 2, 8, 10, 9]
k = 3
print(k_sorted(arr, k))
