'''

https://leetcode.com/problems/search-insert-position/
'''

def search_insert_position(arr, target):

    start = 0
    end = len(arr)-1

    while start < end:

        middle = (start + end)//2

        if arr[middle] == target:
            return middle

        if arr[middle] < target:
            start = middle + 1

        elif arr[middle] > target:
            end = middle -1


    # reaching heremeans target is missing, so we need to find its possibel index

    if arr[start] == target:
        return start

    if arr[start] > target:
        if start == 0:
            return 0

        return start
    else:
        return start + 1


arr = [1,3,5,6]
arr = [1,3]
target = 2

print(search_insert_position(arr,target))

