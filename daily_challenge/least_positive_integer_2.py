"""
https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/?envType=daily-question&envId=2024-05-02
"""


def find_max_k(nums):
    hash_map = {}
    max_k = -1
    for item in nums:
        # if the item is already in hash map, just continue
        if item in hash_map:
            continue
        # check if the opposite sign item is present in hash map
        # if yes then compare it with the last max_k and update max value in max_k
        if -item in hash_map:
            max_k = max(max_k, abs(item))
        # else just add the item as it is in the hash map
        else:
            hash_map[item] = 1

    return max_k


nums = [-1, 2, -3, 3]
nums = [-1,10,6,7,-7,1]
# nums = [-104, -449, -318, -930, -195, 579, -410, 822, -814, -388, -863, 174, -814, 919, -877, 993, 741, 741, -623, -4,
#         -4, 542, 997, 239, 447, -317, 409, -487, -34, 6, -914, 607, -622, 915, 573, 666, -229, 165, 841, -820, 703]

print(find_max_k(nums))
