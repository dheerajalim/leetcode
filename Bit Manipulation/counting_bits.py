"""
Calculate the count of set bits (1's) in the binary representation of the number
"""


def count_bits(n: int):
    # initializing the result with 0 for n =0 , as this will always be 0 count
    result = [0]
    # starting from the index 1
    for i in range(1, n + 1):
        # we then do the & operation of i and i-1, as this will remove the last 1
        # from binary rep of i and since our result has already stored count of 1's
        # for all the previous numbers
        result.append(result[i & (i - 1)] + 1)
    return result


n = 5
print(count_bits(n))
