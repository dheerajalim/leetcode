"""
Return True if the number given is result of  power of 2

2^0 = 1
2 ^ 1 = 2
2 ^ 2 = 4
2 ^ 3 = 8
2 ^ 4 = 16


2,4,8,16,32 ..... will return True else False

Also notice that numbers which are result of power of 2 will always have 1 set bit
hence when we do = n & (n-1), that one set bit will also become 0, hence it will become decimal 0
"""


def power_two(num):
    return num & (num - 1) == 0


num = 16
print(power_two(num))
