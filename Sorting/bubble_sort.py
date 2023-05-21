'''
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.
This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

Bubble SORT compares two elements at a time and based on this swap them,
Therefore in one iteration, the largets element is at the last
The next iteration then runs on the n-1 unsorted array

Complexity Analysis of Insertion Sort:
Bubble sort has a time complexity of O(n^2) which makes it very slow for large data sets.
'''


def bubble_sort(arr):

    n = len(arr)

    while n > 0:

        for i in range(0, n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

        n = n-1

    return arr

arr = [13,46,24,52,20,9]
arr = [5,4,3,2,1]
print(bubble_sort(arr))


def recursive_bubble(arr, i, n):

    if i == n:
        return

    if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]

    recursive_bubble(arr, i+1, n)


def recursive_bubble_sort(arr, n):

    if n == 0:
        return

    recursive_bubble(arr, 0, n-1)

    recursive_bubble_sort(arr, n-1)


a = [7, 6, 5, 4, 3, 3, 2, 1]
recursive_bubble_sort(a, len(a))
print(a)
