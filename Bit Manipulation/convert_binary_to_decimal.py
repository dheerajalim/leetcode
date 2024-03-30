"""
The binary to decimal conversion is done by
taking the 1's and 0's in right to left order and then
multiplying it by 2^(index)

example :
1 1 0 1 -- > 13
so we from right to left multiply it with 2 ^ index

index : 3 2 1 0
13 :    1 1 0 1

this is from right to left
1 * 2^0 + 0 * 2^1 + 1 * 2^2 + 1 * 2^3 = 1 + 0 + 4 + 8 = 13
"""


def binary_to_decimal(binary):
    binary = "".join(reversed(binary))
    result = 0
    for i, j in enumerate(binary):
        result += int(j) * 2 ** i

    return result


binary = "1101"
print(binary_to_decimal(binary))
