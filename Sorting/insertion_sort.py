'''
Algorithm

To sort an array of size n in ascending order:

1: Iterate from arr[1] to arr[n] over the array.

2: Compare the current element (key) to its predecessor.

3: If the key element is smaller than its predecessor, compare it to the elements before.
Move the greater elements one position up to make space for the swapped element

Complexity Analysis of Insertion Sort:
Time Complexity of Insertion Sort
The worst case time complexity of Insertion sort is O(N^2)
The average case time complexity of Insertion sort is O(N^2)
The time complexity of the best case is O(N).
'''


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):

        for j in range(i - 1, -1, -1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            else:
                break

    return arr


arr = [13, 46, 24, 52, 20, 9]
arr = [5, 4, 3, 2, 1]
print(insertion_sort(arr))


# recursive insertion sort

def recursion_insertion_sort(arr, i):

    if i == 0:
        return

    if arr[i-1] > arr[i]:
        arr[i-1], arr[i] = arr[i], arr[i-1]

    recursion_insertion_sort(arr, i-1)


def insertion_sort_recursive(arr, i):

    if i == len(arr):
        return

    recursion_insertion_sort(arr, i)

    insertion_sort_recursive(arr, i+1)

arr = [5, 4, 3, 2, 1]
arr = [13, 46, 24, 52, 20, 9]
insertion_sort_recursive(arr,0)
print(arr)
