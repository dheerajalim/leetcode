def check(arr):

    prev = arr[0]

    for i in range(1, len(arr)):

        if arr[i] >= prev:
            prev = arr[i]

        else:
            return arr[i:] + arr[0:i] == sorted(arr)


    return True


arr = [3,4,5,1,2]

print(check(arr))