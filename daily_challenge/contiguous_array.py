"""
https://leetcode.com/problems/contiguous-array/description/
"""


def find_max_length(nums):

    n = len(nums)

    hash_map = {}

    max_len = 0

    prefix_sum = 0

    for i in range(n):

        if nums[i] == 1:
            prefix_sum += 1
        else:
            prefix_sum -= 1

        if prefix_sum == 0:
            max_len = max(max_len, i + 1)

        if prefix_sum in hash_map:
            start_index = hash_map[prefix_sum]
            max_len = max(max_len, i - start_index)

        else:
            hash_map[prefix_sum] = i

    return max_len


nums = [0, 1, 0]

print(find_max_length(nums))
