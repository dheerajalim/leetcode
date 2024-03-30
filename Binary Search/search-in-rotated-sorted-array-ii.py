"""

https://leetcode.com/problems/search-in-rotated-sorted-array-ii/solutions/

This problem has repeated elements in array
"""


def search( arr, target) :
    start = 0
    end = len(arr) - 1

    while start <= end:

        middle = (start + end) // 2

        if arr[middle] == target:
            return True

        if arr[start] == arr[middle] and arr[middle] == arr[end]:
            start += 1
            end -= 1
            continue

        if arr[start] <= arr[middle]:

            if arr[start] <= target <= arr[middle]:
                end = middle - 1
            else:
                start = middle + 1

        else:
            if arr[middle] <= target <= arr[end]:
                start = middle + 1
            else:
                end = middle - 1

    return False

arr = [3,3,3,1,2,3]
target = 2
arr = [1,0,1,1,1]
target = 0

print(search(arr, target))