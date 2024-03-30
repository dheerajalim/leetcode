"""
To find if the ith bit is set or not
"""


def check_ith(n, i):
    # if we left shift 1 by i times and do the
    # and operation then if the result is 0, then
    # the ith bit is not set else it is set

    # left shift 1 by i time
    left_one = 1 << i

    return n & left_one != 0


n = 13
i = 2

print(check_ith(n, i))
