'''

Complexity : O(N)
'''

def secondLargest(arr):
    # edge case: as there will be less than2 elements, so we cannot have second largest
    if len(arr) <= 1:
        return -1

    # assuming the first element as the largest
    largest = arr[0]
    s_largest = float('-inf')

    for i in range(len(arr)):

        if largest < arr[i]:
            s_largest = largest
            largest = arr[i]

        elif s_largest < arr[i] < largest:
            s_largest = arr[i]

    return s_largest


def seconSmallest(arr):
    smallest = arr[0]
    s_smallest = float('inf')

    for i in range(len(arr)):

        if arr[i] < smallest:
            s_smallest = smallest
            smallest = arr[i]

        elif s_smallest > arr[i] > smallest:
            s_smallest = arr[i]

    return s_smallest


arr = [1, 2, 4, 7, 7, 5]
s_largest = secondLargest(arr)
s_smallest = seconSmallest(arr)
print(s_largest, s_smallest)
