'''

Divide and Conqueo approach

Merge Sort

Best : O(n log(n))

Average: O(n log(n))

Worst : O(n log(n))


Space : O(N) ; as we need an array to store the sorted elements
'''

def merge(arr, start, middle, end , size):

    # creatign an array to store the sorted array after two arrays are merged
    result = [0] * size
    i = start
    j = middle
    k = 0

    while i < middle and j < end:

        if arr[i] < arr[j]:
            result[k] = arr[i]
            i += 1
            k += 1

        else:
            result[k] = arr[j]
            j += 1
            k += 1

    while i < middle:
        result[k] = arr[i]
        i += 1
        k += 1

    while j < end:
        result[k] = arr[j]
        j += 1
        k += 1

    # updating the original array

    for i in range(0, size):
        arr[start+i] = result[i]


def merge_sort(arr, start, end):

    # size is the lenght of the array which if a single element we return as it cannot be sorted

    size = end - start
    if size <= 1:
        return

    middle = (start + end) // 2

    # calling the sorting on two halves
    merge_sort(arr, start, middle)
    merge_sort(arr, middle, end)

    # merge the two halves and sorting them

    merge(arr, start, middle, end, size)


arr = [10,8,2,5,4,1]
merge_sort(arr,0,len(arr))
print(arr)