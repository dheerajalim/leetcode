'''

https://takeuforward.org/arrays/implement-upper-bound/

'''


def upper_bound(arr,n,x):

    ans = n-1

    start = 0
    end = n-1

    while start <= end:
        middle = (start + end) // 2
        if arr[middle] > x:
            ans = middle
            end = middle-1

        else:
            start = middle + 1

    return ans

arr = [1,2,2,3]
n = len(arr)
x = 2


arr = [3,5,8,9,15,19]
n = len(arr)
x = 9

print(upper_bound(arr, n, x))