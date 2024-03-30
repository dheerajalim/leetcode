from collections import deque


def first_negative(arr, n, k):
    i, j = 0, 0
    # to maintian the negative numbers in the array
    negative_list = deque()
    # to store the first -ve of each window
    first_negative = []

    # iterate until the last element of the array
    while j < n:
        # if the item is negative
        # we store it in the negative_list queue
        if arr[j] < 0:
            negative_list.append(arr[j])

            # we increment j until we reach the window size of k
        if j - i + 1 < k:
            j += 1

        # if the window size is acheived
        # we do our calculations
        elif j - i + 1 == k:
            # if the negative list has atleast 1 element
            # then the first element is the first negative of the window
            if len(negative_list):
                first_negative.append(negative_list[0])
            # otherwise the window has no negative number
            else:
                first_negative.append(0)
            # if before shifting the window, the ith index is negative number
            # this means if we shift the window now, this number will no longer be part of
            # any futhure window, so we pop it from the queue as well
            if arr[i] < 0:
                negative_list.popleft()

            # slide the window
            i += 1
            j += 1

    return first_negative


arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
n = len(arr)

print(first_negative(arr, n, k))
