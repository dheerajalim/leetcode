def clear_ith_bit(n, i):
    # this will give a binary number with all 0's
    # only the ith bit is set to 1
    leftshift_one = 1 << i

    # now since we need to clear the ith bit we replace
    # 1 with 0 and 0 with 1 in the leftshift_one
    leftshift_one = ~ leftshift_one

    # now if we do the & operation of leftshift_one and n
    # the ith bit in leftshift_one will be 0 and everything
    # else will be 1 in leftshift_one, this way the ith bit can be cleared

    return n & leftshift_one


n = 13
i = 2

print(clear_ith_bit(n, i))
