import heapq


def kth_largest(arr, k):
    # to find kth largest : use min heap

    # to contain the k largest elements
    result = []

    # iterate through the elements
    for i in arr:

        # push the element to min heap
        heapq.heappush(result, i)

        # if the number of elements in heap are greater than k
        # pop the element, this will pop the smallest element
        if len(result) > k:
            heapq.heappop(result)

    return result


arr = [7, 10, 4, 3, 20, 15]
arr = [3,2,1,5,6,4]
k = 3
print(kth_largest(arr, k))
