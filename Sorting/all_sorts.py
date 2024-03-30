

def selection_sort(arr):
    ''' Search the minimum and place it at the first index'''

    n = len(arr)
    start = 0
    while start != n:
        min_element = arr.index(min(arr[start:n]))
        # swap the min element to make it reach correct position
        arr[start], arr[min_element] = arr[min_element], arr[start]
        start += 1


def insertion_sort(arr):
    ''' Compare the element at index with the leftward elements and swap accordingly'''

    n = len(arr)

    for i in range(1, n):

        for j in range(i-1,-1, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                break


def bubble_sort(arr):
    '''Compare each pair and swap if required, this way each iteration will move the sorted element to last'''
    n = len(arr)
    i = 0
    while n > 0 :

        for i in range(0, n-1):
            if arr[i] >  arr[i+1] :
                arr[i], arr[i+1] = arr[i+1], arr[i]

        n -= 1


def partition(arr, si, ei):
    # taking the last element as the pivot
    pivot = arr[ei]

    i = si  # this is don't to keep the starting as -1, as in loop we need to move i to first element

    for j in range(si,ei):

        if arr[j] <= pivot:

            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[ei] = arr[ei], arr[i]

    return i


def quick_sort(arr, si, ei):
    ''' Select a pivot element and everything around it need to be sorted'''
    if si >= ei:
        return

    pivot = partition(arr, si, ei)

    quick_sort(arr, si, pivot-1)
    quick_sort(arr, pivot+1, ei)


def merge(arr, si, middle, ei, size):


    result = [0] * size
    i = si
    j = middle
    k = 0

    while i < middle and j < ei:

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
        k += 1
        i += 1

    while j < ei:
        result[k] = arr[j]
        k += 1
        j += 1


    for i in range(size):
        arr[si + i] = result[i]



def merge_sort(arr, si , ei):

    size = ei - si

    if size <= 1:
        return

    middle = (si + ei)//2
    merge_sort(arr, si, middle)
    merge_sort(arr, middle, ei)

    merge(arr, si, middle, ei, size)


if __name__ == "__main__":
    arr = [5,4,3,2,1]
    option = input('select option: ')

    if option == '1':
        selection_sort(arr)

    elif option == '2':
        insertion_sort(arr)

    elif option == '3':
        bubble_sort(arr)

    elif option == '4':
        quick_sort(arr, 0, len(arr)-1)

    elif option == '5':
        merge_sort(arr, 0, len(arr))

    print(arr)