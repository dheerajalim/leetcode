"""
https://leetcode.com/problems/number-complement/description/
"""


def find_complement(num):
    binary = bin(num)
    complement = ""
    for i in binary[2:]:
        # if we get the 0, we flip it to 1
        # else flip 1 to 0
        if i == "0":
            complement += "1"
        else:
            complement += "0"

    # convert binary to decimal before returning
    return int(complement, 2)


num = 10

print(find_complement(num))
