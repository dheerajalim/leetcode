"""
Using Binary search to find the peak element.

This is more optimize solution

pre-conditions:
1. If there are multiple peaks, then we just need to find one peak and return the index
2. if len(arr) == 1; then this is the peak already
3. For the first element, we assume that the previous is - inf and for the last element we assume next is -inf
4. so if arr[0] > arr[1]; then arr[0] is peak OR if arr[n-1] > arr[n-2]; then arr[n-1] is peak
5. Hence we can trim our seacrh with start = 1 and end = n-2

"""


def find_peak(arr):

    if len(arr) == 1:
        return 0

    if arr[0] > arr[1]:
        return 0

    if arr[len(arr)-1] > arr[len(arr)-2]:
        return len(arr)-1

    start = 1
    end = len(arr) - 2

    while start <= end:

        middle = (start + end) //2

        if arr[middle-1] < arr[middle] > arr[middle+1]:
            return middle

        if arr[middle] < arr[middle - 1]:
            end = middle - 1

        elif arr[middle] < arr[middle + 1]:
            start = middle + 1

        # the below code was replace by me to reduce the extra else condition , bassically change the check on middle
        # check line 45, 48
        # if arr[middle] > arr[middle-1]:
        #     start = middle + 1
        #
        # elif arr[middle] > arr[middle+1]:
        #     end = middle - 1
        # else:
        #     # this condition is used when we are at the reverse of peak, then we can move either left or right
        #     # start = middle + 1  or end = middle - 1; both can be used
        #     end = middle-1


    return -1

arr =  [1,2,3,1]
arr = [1,2,1,3,5,6,4]
arr = [1,5,1,2,1]
print(find_peak(arr))


