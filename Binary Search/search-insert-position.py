'''

https://leetcode.com/problems/search-insert-position/

Can be solved using Lower Bound of Binary Search
'''

def search_insert_position(arr, n, x):

    start = 0
    end = n-1
    ans = n

    while start <= end:
        middle = (start + end)//2

        if arr[middle] >= x:
            ans = middle
            end = middle-1

        else:
            start = middle + 1

    return ans


arr = [1,2,4,7]
n = len(arr)
x = 2

print(search_insert_position(arr,n, x))

