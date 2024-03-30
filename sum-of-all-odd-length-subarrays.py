def sumOddLengthSubarrays(arr) -> int:
    # arr_length = len(arr)
    # possible_lengths = [i for i in range(1, arr_length + 1, 2)]
    # total_sum = 0
    # for j in possible_lengths:
    #     if j == 1:
    #         total_sum += sum(arr)
    #         continue
    #     if j == len(arr):
    #         total_sum += sum(arr)
    #         continue
    #     k = j
    #
    #     for x in range(arr_length):
    #         if k+x <= arr_length:
    #             total_sum += sum(arr[x:k + x])
    #
    # print(total_sum)

    total = 0

    for i in range(len(arr)):
        cur = 0
        for j in range(i, len(arr), 2):
            if j > i:
                cur += arr[j] + arr[j - 1]
            else:
                cur += arr[j]
            total += cur

    print(total)

arr = [1,4,2,5,3]
sumOddLengthSubarrays(arr)