import heapq


def frequency_count(arr):
    frequency = {}

    for i in arr:
        frequency[i] = 1 + frequency.get(i, 0)

    return frequency


def reorganise_string(string):
    arr = frequency_count(list(string))
    n = len(string)
    pq = []
    result = [""]*n

    for i, j in arr.items():
        heapq.heappush(pq, [-j, i])


    highest_freq = heapq.heappop(pq)

    if -highest_freq[0] > (n + 1)//2:
        return ""

    idx = 0
    for _ in range(-highest_freq[0]):
        result[idx] = highest_freq[1]
        idx += 2

    idx -= 2
    while pq:

        current = heapq.heappop(pq)

        # if idx + 1 >= n:
        #     idx = 1

        for _ in range(-current[0]):
            if idx + 1 >= n-1:
                idx = -1
            idx += 2
            result[idx] = current[1]


    return "".join(result)

string = "bbbaaccdde"
print(reorganise_string(string))
