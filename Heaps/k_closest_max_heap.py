import heapq


def k_closest(arr, x, k):
    # for the heap
    pq = []
    # iterate the array and push to the heap
    # this is a max heap
    # therefore we insert -(ve) items
    for i in arr:
        heapq.heappush(pq, [-abs(i - x), -i])
        # if the length of heap is greater, then
        # we pop the item
        if len(pq) > k:
            heapq.heappop(pq)

    print(pq)
    # we get the items from the heap
    # and return them by making them positive again
    for i in range(len(pq)):
        pq[i] = -pq[i][1]

    # pq has the k closest elements
    # if required sort and return else, return pq only
    return sorted(pq)


arr = [1, 2, 3, 4, 5]
x = 3
k = 4

print(k_closest(arr, x, k))
