from collections import deque


def max_sliding_window(nums, k):
    dq = deque()
    n = len(nums)
    result = []
    i, j = 0, 0
    while j < n:
        # if the window size is not reached
        if j - i + 1 <= k:
            # then keep on adding the item to deque
            # we always want to have the largest item
            # at the 0th index, otherwise we keep on poping
            # if the largest element is not at 0th index of queue
            while dq and nums[dq[-1]] < nums[j]:
                dq.pop()

            # add item to the queue
            dq.append(j)
            # if the window size is reached, then we just
            # get the 0th item from queue and add it to result
            if j - i + 1 == k:
                result.append(nums[dq[0]])
            # slide the window
            j += 1

        # if the window size is greater than k
        else:
            # then remove all the items from the queue
            # which are before the ith index
            # as we will not need them as i will move out
            # of the window
            while dq and dq[0] <= i:
                dq.popleft()

            # slide the ith index to get back the window size == k
            i += 1

    return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
# nums = [1]
# k = 1
# nums = [9, 10, 9, -7, -4, -8, 2, -6]
# k = 5
nums = [1, -1]
k = 1

print(max_sliding_window(nums, k))
