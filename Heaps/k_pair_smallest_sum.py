"""
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
"""
import heapq


def k_smallest_pair(nums1, nums2, k):
    pq = []

    for i in nums1:

        for j in nums2:

            heapq.heappush(pq, [-(i + j), [i, j]])

            if len(pq) > k:
                heapq.heappop(pq)
                break

    result = []
    for i in pq:
        result.append(i[1])
    return result

nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3

# nums1 = [1, 1, 2]
# nums2 = [1, 2, 3]
# k = 2

nums1 = [1,2,4,5,6]
nums2 = [3,5,7,9]
k = 3

print(k_smallest_pair(nums1, nums2, k))
