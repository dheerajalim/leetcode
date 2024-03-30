"""
Given the root node of a binary search tree and two integers low and high,
return the sum of values of all nodes with a value in the inclusive range [low, high].
https://leetcode.com/problems/range-sum-of-bst/
"""

from binary_tree import *


def find_range_sum(root, start, end, range_sum):
    if root is None:
        return 0

    if root.data < start and root.data < end:
        find_range_sum(root.right, start, end, range_sum)

    elif root.data > start and root.data > end:
        find_range_sum(root.left, start, end, range_sum)

    elif start <= root.data <= end:
        range_sum[0] += root.data
        find_range_sum(root.left, start, end, range_sum)
        find_range_sum(root.right, start, end, range_sum)


root = inserttree()
range_sum = [0]
start, end = 7, 15
find_range_sum(root, start, end, range_sum)
print(range_sum[0])
