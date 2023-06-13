'''

Using Binary Search we will solve this problem

At any point of time there will always be a peak in an array , as if three numbsrrs
A, B, C.. atmost the can be same but apart from them someone will be greater than the other

'''


def find_peak(arr):
    start = 0
    end = len(arr) - 1

    while start < end:

        middle = (start + end) // 2

        if middle == 0:  # the first element

            if arr[middle] >= arr[middle + 1]:
                return middle

            else:
                return middle + 1

        if middle == len(arr)-1:  # last element
            if arr[middle] >= arr[middle - 1]:
                return middle
            else:
                return middle - 1

        if arr[middle - 1] <= arr[middle] and arr[middle + 1] <= arr[middle]:
            return middle

        if arr[middle] < arr[middle - 1]:
            end = middle - 1

        elif arr[middle] < arr[middle + 1]:
            start = middle + 1

    return start


arr = [1,2,3]

print(find_peak(arr))
