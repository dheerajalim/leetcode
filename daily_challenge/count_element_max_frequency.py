"""
https://leetcode.com/problems/count-elements-with-maximum-frequency/description/
"""
def max_frequency(nums):
    hash_map = {}
    max_freq = float('-inf')
    max_count = 0

    for i in nums:

        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1

        if hash_map[i] > max_freq:
            max_freq = hash_map[i]
            max_count = hash_map[i]
        elif hash_map[i] == max_freq:
            max_count += hash_map[i]

    return max_count

# Approach 2
"""
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash_map = {}
        max_freq = float('-inf')
        max_count =  0

        for i in nums:

            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

            max_freq = max(max_freq, hash_map[i])

        for v in hash_map.values():
            if v == max_freq:
                max_count += 1

        return max_freq * max_count
"""
nums = [1, 2, 2, 3, 1, 4]
print(max_frequency(nums))
