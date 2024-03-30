def reverse_bits(n: int) -> int:
    ans = 0
    for i in range(32):
        # keep on checking the bits from right to left
        # if the bit is set, then
        # do OR operation with ans and left shift the set bit by 31- i
        if n & 1 << i:
            # this will move the set bit in n to a position which is 31-i
            # example set bit at 3, when reverse will move to 31-3 = 28
            ans = ans | 1 << (31 - i)

    return ans


n = 10

print(reverse_bits(n))
