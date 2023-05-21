def is_array_sorted(arr):

    result = True
    for i in range(len(arr) - 1):

        if arr[i] > arr[i+1]:
            result = False
            break

    return result

arr = [1,2,3,4,5]
arr = [5,4,6,7,8]
print(is_array_sorted(arr))