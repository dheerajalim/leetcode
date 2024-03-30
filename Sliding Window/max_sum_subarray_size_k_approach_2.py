def max_subarray_sum(arr, n, k):
    # keep the i and j at the 0th index
    i, j = 0, 0
    # to store the max sum
    max_sum = 0
    # to store the sum of the window
    k_sum = 0
    # iterate until we reach the last index/or last window
    # of size k
    while j < n:
        # keep on adding the jth index value to the window sum
        k_sum += arr[j]
        # we need to reach the k size window
        # so we keep on increasing th jth index
        if j - i + 1 < k:
            j += 1
        # if the window size is equal to k
        # then we compare the window sum with max sum and store the max sum
        # remove the ith index value from sum and increment i and j
        # this now maintains the window size and just slides the window
        # Notice: the value from new jth index is added at the line 12 in each iteration
        # hence we do not add that here
        elif j - i + 1 == k:
            max_sum = max(max_sum, k_sum)
            k_sum -= arr[i]
            i += 1
            j += 1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
n = len(arr)

print(max_subarray_sum(arr, n, k))
