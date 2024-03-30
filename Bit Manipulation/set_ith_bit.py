def set_ith_bit(n, i):
    # left shift 1 by i
    leftshift_one = 1 << i

    # hence the ith position after left shift will have 1
    # when we do the OR operation of left shifted number with n
    # if the ith position in n has 0, it will give 1 after or operation with 1
    # else if the ith position in n has 1, it will still give 1 as we are doing
    # or operation
    # example : 9 = 1 0 0 1, i = 2
    # i << 2 = 0 1 0 0
    # OR OPERATION : 1 0 0 1
    #                0 1 0 0
    #               =1 1 0 1
    result = n | leftshift_one

    return result
