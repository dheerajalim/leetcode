"""
1's Complement : Flip the bits : 1001 --> 0110
2's complement : Find 1's complement -- > Add 1 --> Gives 2's complement

Right shift :

x >> k = (x // 2 ^k)
13 >> 2 = (13 // 2^2) = (13//4) = 3

Left Shift
x << k = x * 2 ^ k
13 << 1 = (13 * 2^1) = 26

Not operator = ~

~ x :
1. Flip the bits
2. If the number is negative after flipping
    YES : The find 2's complement
    NO : Return the number after flipping
"""