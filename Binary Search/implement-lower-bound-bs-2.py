'''
https://takeuforward.org/arrays/implement-lower-bound-bs-2/

Use Binary Search , since the lower bound is the smallest index value that is greater than the given x, hence
once we find the middle that is >= x, we will search on the left size to see if any other smaller index also satisfies
the >=x condition
'''


def find_lower_bound(arr,start, end, x, ans):

    if start > end:
        return None

    middle = (start + end)//2

    if arr[middle] >= x:
        ans[0] = middle
        return find_lower_bound(arr, start, middle-1, x, ans)

    else:
        return find_lower_bound(arr, middle + 1, end, x, ans)

    return ans



def lower_bound(arr, n, x):

    start = 0
    end = n-1
    ans = [n]
    find_lower_bound(arr, start, end, x, ans)

    return ans[0]



arr = [1,2,2,3]
n = len(arr)
x = 2

arr = [3,5,10,11,15,19]
n = len(arr)
x = 9

arr = [3,5,8,9,15,19]
n = len(arr)
x = 9

print(lower_bound(arr,n,x))