"""
https://leetcode.com/problems/k-th-smallest-prime-fraction/description/?envType=daily-question&envId=2024-05-10

This is an O(n^2) solution
"""

import heapq

def kth_smallest_prime_fraction(arr, k):

    pq = []

    # we iterate in two loops to get the fraction of all possible combinations
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):

            fraction = arr[i] / arr[j]

            # we create a max heap and add the fraction value along with the num and denominator
            heapq.heappush(pq, (-fraction, [arr[i], arr[j]]))

            # if the size of heap becomes greater than k , then we pop the item from heap
            if len(pq) > k:
                heapq.heappop(pq)

    return heapq.heappop(pq)[1]


arr = [1,7]
k = 1

print(kth_smallest_prime_fraction(arr, k))