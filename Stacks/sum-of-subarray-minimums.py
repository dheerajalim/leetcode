# https://leetcode.com/problems/sum-of-subarray-minimums/description/

"""
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.



Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

"""


# Solving using the Maximum Area of Histogram

def mah(arr):
    n = len(arr)
    stack_left, stack_right = [], []
    stack_left_index, stack_right_index = [], [n] * n

    i, j = 0, n - 1

    # for the left index

    while i < n:

        while stack_left and arr[i] <= stack_left[-1][0]:
            stack_left.pop()

        if stack_left:
            stack_left_index.append(stack_left[-1][1])
            stack_left.append((arr[i], i))

        else:
            stack_left_index.append(-1)
            stack_left.append((arr[i], i))

        i += 1
    # for the right index

    while j >= 0:
        # please note that we are using < and not <= here
        # this is to avoid the same number being counted
        # on both left and right side
        while stack_right and arr[j] < stack_right[-1][0]:
            stack_right.pop()

        if stack_right:
            stack_right_index[j] = stack_right[-1][1]
            stack_right.append((arr[j], j))

        else:
            stack_right_index[j] = n
            stack_right.append((arr[j], j))

        j -= 1

    return stack_right_index, stack_left_index


def sum_subarray_min(arr):
    # gives the left and right index using Max Area of Histogram
    stack_right_index, stack_left_index = mah(arr)
    result = 0
    for i in range(len(arr)):
        # we apply the formula
        # M = NSE Right Index - Current Index
        stack_right_index[i] = stack_right_index[i] - i
        # N = Current Index - NSE Index Left
        stack_left_index[i] = i - stack_left_index[i]

        # The result is the summation of (M * N) * arr[i]
        result += stack_right_index[i] * stack_left_index[i] * arr[i]

    return result


arr = [3, 1, 2, 4]
arr = [71,55,82,55]

print(sum_subarray_min(arr))

# for the left index
