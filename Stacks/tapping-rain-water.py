def tapping_rain_water(arr):
    n = len(arr)
    # creating the two stacks
    max_left, max_right = [0] * n, [0] * n
    # initializing the first and last index of stacks
    # as the first and last will have themselves as max
    max_left[0], max_right[-1] = arr[0], arr[-1]

    i, j = 1, len(arr) - 2

    # iterating through the array in 0 to n and n to 0 order
    while i <= len(arr) - 1 and j >= 0:
        # for each index calculating the left and right max
        max_left[i] = max(max_left[i - 1], arr[i])
        max_right[j] = max(arr[j], max_right[j + 1])
        i += 1
        j -= 1

    result = 0
    # for each index calculating the min(max_left[i], max_right[i]) - arr[i]
    for i in range(n - 1):
        result += min(max_left[i], max_right[i]) - arr[i]

    return result


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(tapping_rain_water(arr))
