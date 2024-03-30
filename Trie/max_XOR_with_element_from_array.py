"""
https://leetcode.com/problems/maximum-xor-with-an-element-from-array/description/
"""


class TrieNode:

    def __init__(self):
        self.childNode = [None] * 2


class Trie:

    def __init__(self):

        self.root = TrieNode()

    def insert(self, number):

        node = self.root
        # since the input int is give to be +ve
        # hence we just make it 32 bit, zfill add the 0's
        # as prefix till the specified length
        binary_num = bin(number)[2:].zfill(32)

        # now we add each bit to the trie
        for num in binary_num:
            num = int(num)
            if node.childNode[num] is None:
                node.childNode[num] = TrieNode()

            node = node.childNode[num]

    def find_max_xor(self, xor_with):
        # we now calculate the XOR of given number
        # with each item in the input nums
        # and get the maximum XOR result
        node = self.root
        # converting xor_with to binary
        xor_binary_num = bin(xor_with)[2:].zfill(32)
        # to store the  max XOR result
        max_num = ""

        for num in xor_binary_num:
            num = int(num)
            # the max possible answer will come if we
            # XOR it with a  opposite bit i.e 0 with 1 or 1 with 0

            # flipping the bit to check if it exists
            xor_num = 1 - num
            # if the flipped bit exists
            # then we just store the flipped bit
            if node.childNode[xor_num]:
                max_num += str(xor_num)
                # and update the next node to this node
                num = xor_num
            # else if the flipped bit does not exists, in that case
            # we add the same available bit
            else:
                max_num += str(num)

            node = node.childNode[num]

        # return the XOR of input number and max_num
        return int(max_num, 2) ^ xor_with


def maximize_xor(nums, queries):
    trie = Trie()

    nums = sorted(nums)

    result = [-1] * len(queries)
    [query.append(i) for i, query in enumerate(queries)]
    queries = sorted(queries, key=lambda x: x[1])

    pos = 0
    for xi, mi, index in queries:

        if nums[0] > mi:
            result[index] = -1
            continue
        while pos < len(nums) and nums[pos] <= mi:
            trie.insert(nums[pos])
            pos += 1

        current_max_xor = trie.find_max_xor(xi)

        # we store the max_xor result
        result[index] = current_max_xor

    return result


nums = [0, 1, 2, 3, 4]
queries = [[3, 1], [1, 3], [5, 6]]
#
# nums = [5, 2, 4, 6, 6, 3]
# queries = [[12, 4], [8, 1], [6, 3]]

print(maximize_xor(nums, queries))
