'''

Idea is to use bnary search for findung the occurance of the target
Once we know a index of the target then we for left and right to see the total occurance of the target

Time Complexity: O(logN)

Space Complexity: O(1)


'''


def first_occurnce(arr, target, start, end):
    while start <= end:

        middle = (start + end) // 2

        if arr[middle] == target:

            return middle

        elif arr[middle] > target:
            end = middle - 1

        elif arr[middle] < target:
            start = middle + 1

    return -1


def count_occurance(arr, target):
    start = 0
    end = len(arr) - 1
    middle = first_occurnce(arr, target, start, end)

    if middle == -1:
        return 0

    occurance = 1

    right_occur = middle + 1
    left_occur = middle - 1

    while right_occur < end:

        if arr[right_occur] == target:
            occurance += 1
            right_occur += 1
        else:
            break

    while left_occur > start:

        if arr[left_occur] == target:
            occurance += 1
            left_occur -= 1
        else:
            break

    return occurance


arr = [2, 2, 3, 3, 3, 3, 4]
target = 3
occurance = count_occurance(arr, target)
print(occurance)
