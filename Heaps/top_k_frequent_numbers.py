"""
Use Min heap : Identification Top K elements /largest/ greatest
"""
import heapq


def get_freq(arr):
    # to get the frequency of each element
    # this will store {arr[i] : frequency}
    hash_map = dict()

    for i in arr:
        if hash_map.get(i):
            hash_map[i] += 1
        else:
            hash_map[i] = 1

    return hash_map


def top_k_frequent(arr, k):
    # contains the frequency of each element
    freq_map = get_freq(arr)

    # create the min heap
    pq = []
    # iterate through the hash map
    for i, j in freq_map.items():
        # the key in heap is the frequency
        # heap = {frequency , arr[i]}
        heapq.heappush(pq, (j, i))
        # if the heap > k , the pop the top element
        # the top element is the min element
        if len(pq) > k:
            heapq.heappop(pq)

    # the pq has the largest k elements based on frequency
    # fetch the arr[i] frpm hea[
    for i in range(len(pq)):
        pq[i] = pq[i][1]

    # return the top k frequency
    return pq


arr = [1, 1, 1, 3, 2, 2, 4]
k = 2
print(top_k_frequent(arr, k))
