'''

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

https://takeuforward.org/data-structure/minimum-in-rotated-sorted-array/

'''

def find_minimum(arr):

    start = 0
    end = len(arr) - 1

    min_value = float('+inf')
    while start <= end:
        # optimization , this means the array is sorted
        if arr[start] <= arr[end]:
            min_value = min(arr[start], min_value)
            break

        middle = (start + end) //2

        if arr[start] <= arr[middle]:
            min_value = min(arr[start], min_value)
            start = middle + 1

        else:
            min_value = min(arr[middle], min_value)
            end = middle - 1


    return min_value


arr = [3,4,5,1,2]
arr = [4,5,6,7,0,1,2]
# arr = [1,2,3,4]
print(find_minimum(arr))
