'''

Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest)
 element from the unsorted portion of the list and moving it to the sorted portion of the list.

 <SELECT MINIMUM AND SWAP IT WITH THE FIRST UNSORTED ELEMENT>

 Disadvantages of the Selection Sort Algorithm
Selection sort has a time complexity of O(n^2) in the worst and average case.
Does not work well on large datasets.
'''


def selection_sort(arr):

    start = 0
    n = len(arr)-1

    while start != n:
        min_element = arr.index(min(arr[start:n+1]))

        arr[start], arr[min_element] = arr[min_element], arr[start]

        start += 1

    return arr


arr = [13,46,24,52,20,9]
arr = [5,4,3,2,1]
print(selection_sort(arr))




