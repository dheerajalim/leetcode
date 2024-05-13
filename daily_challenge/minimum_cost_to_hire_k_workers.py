"""
https://leetcode.com/problems/minimum-cost-to-hire-k-workers/?envType=daily-question&envId=2024-05-11

Manager = A person who we take as reference to have the salary decided for others
"""
import heapq


def min_cost_to_hire(quality, wage, k):
    # we will first store the ratio of wage/quality

    wbyq_ratio = []  # store ration and quality
    for i, j in zip(wage, quality):
        wbyq_ratio.append((i / j, j))
    print(wbyq_ratio)
    # now we sort the wage/quality ratio, this is done so that we can take the k workers
    # who have w/q ratio less than the person we select
    wbyq_ratio = sorted(wbyq_ratio)

    # we now start the loop from  k-1 , as we need k workers
    start = k - 1

    # pq for the storage of k workers quality
    pq = []
    quality_sum = 0
    i = 0
    result = float('inf')
    while start < len(wbyq_ratio):
        # we start from the worked who can be potential manager
        manager_ratio = wbyq_ratio[start][0]
        while i <= start:
            # then we just keep in adding the quality of each worker
            # who are before manager,as their ratio is less
            heapq.heappush(pq, -wbyq_ratio[i][1])
            poped = 0
            # maintina a max heap of size k
            if len(pq) > k:
                poped = heapq.heappop(pq)

            # every time we have heap size greater than k worker, then we pop the highest quality worker
            # value as this will help us to reduce the total amount of wages
            quality_sum += wbyq_ratio[i][1] - (-poped)
            i += 1
        # storing the min of wages
        result = min(result, manager_ratio * quality_sum)

        start += 1
    return result


quality = [10, 20, 5]
wage = [70, 50, 30]
k = 2

quality = [3, 1, 10, 10, 1]
wage = [4, 8, 2, 2, 7]
k = 3
print(min_cost_to_hire(quality, wage, k))
