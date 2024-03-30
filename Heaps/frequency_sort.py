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


def frequency_sort(arr):
    # contains the frequency of each element
    freq_map = get_freq(arr)

    # create the max heap
    pq = []
    result = []
    # iterate through the hash map
    for i, j in freq_map.items():
        # the key in heap is the frequency
        # heap = {frequency , arr[i]}
        heapq.heappush(pq, (-j, i))

    # pop the item from the heap
    while pq:
        freq, element = heapq.heappop(pq)
        # insert element into the result array freq times
        # since this is max heap, highest frequency element is at top
        # also we remove the -ve sign (python constraint for max heap)
        for _ in range(-freq):
            result.append(element)

    return result


arr = [1, 1, 1, 3, 2, 2, 4]
arr = ['t', 'r', 'e', 'e']
arr = ['c','c','c','a','a','a']
print(frequency_sort(arr))
