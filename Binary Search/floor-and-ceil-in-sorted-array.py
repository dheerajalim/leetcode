"""
https://takeuforward.org/arrays/floor-and-ceil-in-sorted-array/

Problem Statement: You’re given an unsorted array arr of n integers and an integer x. Find the floor and ceiling of x in arr[0..n-1].
The floor of x is the largest element in the array which is smaller than or equal to x.
The ceiling of x is the smallest element in the array greater than or equal to x.

"""


def floor(arr, x, n):

    start = 0
    end = n-1
    ans = -1

    while start <= end:
        middle = (start + end) // 2

        if arr[middle] <= x:
            ans = arr[middle]
            start = middle + 1

        elif arr[middle] > x:
            end = middle - 1

    return ans


def ceil(arr, x, n):

    start = 0
    end = n-1
    ans = -1

    while start <= end:
        middle = (start + end) // 2

        if arr[middle] >= x:
            ans = arr[middle]
            end = middle-1

        elif arr[middle] < x:
            start = middle + 1

    return ans




def find_floor_ceil(arr,x):

    n = len(arr)

    print(floor(arr,x,n))
    print(ceil(arr,x,n))


arr = [3, 4, 4, 7, 8, 10]
x = 5
x = 8
find_floor_ceil(arr,x)

