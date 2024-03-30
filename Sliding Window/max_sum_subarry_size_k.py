def max_subarray_sum(arr, n, k):
    # taking the size of the array
    size = n - 1
    # taking the initial window of size k and its sum
    k_sum = sum(arr[0: k])
    # initializing the max sum as the sum of initial window
    max_sum = k_sum
    # since we need to move the window by 1 size on the right
    # keep i =1 and j =k or example intially window was 0,1,2
    # now it will be 1,2,3
    i, j = 1, k
    # iterate until pointer j points to last index
    # as we need to maintain the window size and not go outside array size
    while j <= size:
        # we subtract the i-1 index value from the k_sum and add the j index value
        # example 1,2,3,4,5,6 => first window  : 1+2+3 = 6
        # second window = 2 + 3 + 4 == > 6 -2 + arr[j]
        k_sum = k_sum - arr[i - 1] + arr[j]

        # update the max subarray sum
        max_sum = max(max_sum, k_sum)
        # keep sliding the window
        i += 1
        j += 1

    return max_sum


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 2
n = len(arr)

print(max_subarray_sum(arr, n, k))
