'''
https://takeuforward.org/data-structure/last-occurrence-in-a-sorted-array/

Similary algo to Binary Search, only thing is if we find the elemet, we move leftwards as we need to find the lasst occurance

Time Complexity: O(log n)

Space Complexity: O(1)

'''


def last_occurance_bs(arr, element, start, end):
    result = -1

    while start <= end:

        middle = (start + end) // 2

        if arr[middle] == element:
            result = middle
            start = middle + 1

        elif arr[middle] < element:
            start = middle + 1

        elif arr[middle] > element:
            end = middle - 1

    return result


arr = [3, 4, 13, 13, 13, 20, 40]
element = 13

print(last_occurance_bs(arr, element, 0, len(arr) - 1))
