# Max Heap --> Smallest elements
import heapq


def kth_smallest(arr, k):
    # to find kth smallest : use max heap
    # to contain the k smallest elements
    result = []

    for i in arr:
        # push the element to max heap
        # since by default python implements min heap
        # we pass elements as negative
        heapq.heappush(result, -1 * i)
        # if the number of elements in heap are greater than k
        # pop the element, this will pop the largest element
        if len(result) > k:
            heapq.heappop(result)
    # convert back to positive
    return [-i for i in result]


arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_smallest(arr, k))
