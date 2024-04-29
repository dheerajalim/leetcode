"""
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/?envType=daily-question&envId=2024-04-29

The idea is to do the XOR of all items in nums and then check the difference in bits of K and XOR result
The difference of bits is the result as we know that to get k from xor of all items, we would need to flip the bits
in the result of xor of all items
"""


# Solution 1
def calculate_operations(xor_result, k):
    # to get the count of bits that differ in k an d xor_result
    count = 0
    # getting the binary representation
    xor_result_binary = bin(xor_result)[2:]
    k_binary = bin(k)[2:]

    # checking the length of the binary and attaching required 0 as prefix
    if len(xor_result_binary) > len(k_binary):
        len_diff = len(xor_result_binary) - len(k_binary)
        k_binary = "0" * len_diff + k_binary

    else:
        len_diff = len(k_binary) - len(xor_result_binary)
        xor_result_binary = "0" * len_diff + xor_result_binary

    # checking how many bits differ and updating the count
    for i, j in zip(xor_result_binary, k_binary):
        if i != j:
            count += 1

    return count


def min_operations(nums, k):
    # in case the nums has only 1 element, then
    # we directly perform the calculations
    if len(nums) == 1:
        count = calculate_operations(nums[0], k)

    # otherwise we calculate the xor of all the items in nums
    else:
        xor_result = nums[0]
        for i in range(1, len(nums)):
            xor_result = xor_result ^ nums[i]

        # now we do the calculation in the xor of all elements and K
        count = calculate_operations(xor_result, k)

    return count


nums = [2, 1, 3, 4]
k = 1

# print(min_operations(nums, k))


# Solution 2

def min_operations_2(nums, k):
    count = 0
    xor_result = nums[0]
    for i in range(1, len(nums)):
        xor_result = xor_result ^ nums[i]

    # since we have 32 bits for the number we compare each bit of K and xor_result
    # by doing the left shift operation on each bit, if they do not match then we increment the count
    for i in range(0, 32):
        if (k & (1 << i)) != (xor_result & (1 << i)):
            count += 1

    return count

nums = [2,0,2,0]
k = 0

print(min_operations_2(nums, k))
