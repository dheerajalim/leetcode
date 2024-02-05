"""
give k1 and k2, find the k1 smallest and
k2 smallest element in the array and return
sum of elements between k1 and k2 smallest
"""
import heapq


def k_smallest(arr, k):
    # using max heap to get the kth smallest
    pq = []

    for i in arr:
        heapq.heappush(pq, -i)

        if len(pq) > k:
            heapq.heappop(pq)

    return -pq[0]


def sum_k1_k2(arr, k1, k2):
    # get the k1 and k2 smallest using max heap
    k1_smallest = k_smallest(arr, k1)
    k2_smallest = k_smallest(arr, k2)
    total_sum = 0
    # iterate through the array to get
    # the number between k1 and k2 smallest
    for i in arr:
        if k1_smallest < i < k2_smallest:
            total_sum += i

    # return the total sum
    return total_sum


arr = [1, 3, 12, 5, 15, 11]
k1, k2 = 3, 6
print(sum_k1_k2(arr, k1, k2))
