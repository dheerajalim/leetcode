"""
The idea here is to only iterate for the set bits and not for all the bits

In side the while loop we keep on reducing the number by using
n & (n-1) , when we subtract 1 from n, then the last set bit becomes 0
and all the bits after that will become 1

40 = 101000
39 = 100111
&  = 100000
All bits after the last 1 in 40 become 1 in 39 and last set bit becomes 0
This way we count the set bits
"""


def brain_k(n):
    result = 0
    while n:
        # here the last set bit in n becomes:
        # 0 and all bits after that become 1 in n-1, so the & operation
        # basically converts everything including last set bit in n to 0
        # this way we keep on removing the set bits and incrementing the result counter
        n = n & (n - 1)
        result += 1

    return result


n = 13
print(brain_k(n))
