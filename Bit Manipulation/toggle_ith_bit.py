def toggle_bits(n, i):
    leftshift_one = 1 << i

    return n ^ leftshift_one


n = 13
i = 2

print(toggle_bits(n, i))
