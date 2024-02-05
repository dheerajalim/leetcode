import heapq

def find_median(arr):

    result = []
    pq = []
    for i in range(len(arr)):

        heapq.heappush(pq, arr[i])

        if i % 2 == 0:
            result.append(pq[i//2])

        else:

            result.append((pq[i//2] +  pq[i//2+1])/2)

    print(result)

arr = [25, 7, 10, 15, 20]

find_median(arr)

