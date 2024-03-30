"""
TC : O(N * 32) + O(M * 32), we insert N nums forst, then we iterate over M nums to get the XOR
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


def max_xor(nums):
    trie = Trie()
    for num in nums:
        # insert each integer in the trie
        trie.insert(num)

    max_xor = 0

    for num in nums:
        # we iterate through each item of the input nums
        # and then take one item at a time and find the max possible XOR
        current_max_xor = trie.find_max_xor(num)

        # we store the max_xor result
        max_xor = max(max_xor, current_max_xor)

    return max_xor


nums = [3, 10, 5, 25, 2, 8]
nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]

print(max_xor(nums))
