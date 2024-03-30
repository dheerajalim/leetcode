def pivot_element(n):

    arr = [i for i in range(1, n + 1)]

    if len(arr) == 1:
        return arr[0]

    i, j = 1, n - 2

    prefix_i, prefix_j = arr[0], arr[-1]

    while i < j:


        if prefix_i <= prefix_j:
            prefix_i += arr[i]
            i += 1

        elif prefix_j < prefix_i:
            prefix_j += arr[j]
            j -= 1

    if prefix_i == prefix_j:
        return arr[i]

    return -1


n = 49
print(pivot_element(n))
