"""
This can be solved using Max heap
In the heap we store the abs difference of the |x - element|
Heap = (abs diff, element)
"""

###
"""
Since this solution requires making max heap on a pair
python behaves different
If two tuples (a1, b1) and (a2, b2) are being compared:
First, Python compares a1 with a2.
If a1 is less than a2, (a1, b1) comes before (a2, b2) in the heap.
If a1 is equal to a2, Python compares b1 with b2. If b1 is less than b2, (a1, b1) comes before (a2, b2).

Hence the result is wrong
"""
###
import heapq


# wrong answer in python using max heap
# def k_closest(arr, x, k):
#     pq = []
#     for i in arr:
#         heapq.heappush(pq, [-abs(i - x), i])
#
#         if len(pq) > k:
#             heapq.heappop(pq)
#
#     return pq


# solution using min heap

def k_closest(arr, x, k):
    # for the heap
    pq = []
    # to store the k closest
    result = []
    # insert the item to the min heap
    for i in arr:
        # the smallest item is on the top
        # we store the abs difference and arr[i]
        heapq.heappush(pq, [abs(i - x), i])

    # once all the items are in the heap
    # we keep on popping from the heap
    # to get the k closest
    while k > 0:
        result.append(heapq.heappop(pq)[1])
        k -= 1

    # result has the k closest elements
    # if required sort and return else, return result only
    return sorted(result)


arr = [5, 6, 7, 8, 9]
x = 7
k = 3
arr = [1, 2, 3, 4, 5]
x = 3
k = 4

print(k_closest(arr, x, k))
