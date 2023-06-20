'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Can be solved Using Binary Search ... once we find the element, we move towards left to get the first occurance
Time Complexity: O(log n)

Space Complexity: O(1)

'''


def first_occurance_bs(arr, x, start, end):

    result = -1

    while start <= end:

        middle = (start + end) // 2

        if arr[middle] == x:
            result = middle
            end = middle - 1

        elif arr[middle] < x:
            start = middle + 1

        elif arr[middle] > x:
            end = middle - 1

    return result


arr = [3, 4, 13, 13, 13, 20, 40]
x = 13
arr =[]
x = 0

print(first_occurance_bs(arr, x, 0, len(arr) - 1))
