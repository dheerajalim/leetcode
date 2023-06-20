def first_occurance_bs(arr, x, start, end):

    result = -1

    while start <= end:

        middle = (start + end) // 2

        if arr[middle] == x:
            result = middle
            end = middle - 1

        elif arr[middle] < x:
            start = middle + 1

        elif arr[middle] > x:
            end = middle - 1

    return result


def last_occurance_bs(arr, x, start, end):
    result = -1

    while start <= end:

        middle = (start + end) // 2

        if arr[middle] == x:
            result = middle
            start = middle + 1

        elif arr[middle] < x:
            start = middle + 1

        elif arr[middle] > x:
            end = middle - 1

    return result


def find_count(arr,x):

    start =0
    end = len(arr) - 1
    first = first_occurance_bs(arr,x,start,end)
    if first == -1:
        return 0
    last = last_occurance_bs(arr,x,start,end)
    return (last - first) + 1


arr = [2, 2 , 3 , 3 , 3 , 3 , 4]
x = 3
arr = [1, 1, 2, 2, 2, 2, 2, 3]
x = 2
arr = [1, 1, 2, 2, 2, 2, 2, 3]
x = 10

print(find_count(arr,x))

