def min_flips(start, goal):
    # XOR of numbers
    res = start ^ goal

    # this will give 1 for all the bits that differ
    # then we calculate the set bits
    count = 0
    while res:
        res = res & res - 1
        count += 1

    return count
