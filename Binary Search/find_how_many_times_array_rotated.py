"""

https://www.youtube.com/watch?v=jtSiWTPLwd0

The concept is to use the Binary search to find the minimum element's index. and the index at which the minimum
element is present is the time the array is rotated

Example:
    [4,5,1,2,3]
Min element = 1 , Index = 2
Hence array is rotated 2 times

    [1, 2, 3 , 4 ,5]
Min element = 1 , Index = 0
Hence array is rotated 0 times

"""


def find_rotation(arr):

    start = 0
    end = len(arr) - 1
    min_index = -1
    min_value = float('+inf')

    while start <= end:

        middle = (start + end) // 2

        # condition to optimize

        if arr[start] <= arr[end]:
            if arr[start] < min_value:
                min_index = start
                min_value = arr[start]
                break

        if arr[start] <= arr[middle]:
            if arr[start] < min_value:
                min_index = start
                min_value = arr[start]
            start = middle + 1

        else:
            if arr[middle] < min_value:
                min_index = middle
                min_value = arr[middle]
            end = middle - 1

    return min_index


arr = [ 3,4,5,1,2]

print(find_rotation(arr))
