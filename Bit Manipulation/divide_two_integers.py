"""
https://leetcode.com/problems/divide-two-integers/description/
"""


def divide(dividend: int, divisor: int):
    sign = True  # + ve
    if dividend >= 0 and divisor < 0:
        sign = False

    if dividend < 0 and divisor > 0:
        sign = False

    result = 0
    dividend = abs(dividend)
    divisor = abs(divisor)
    while dividend >= divisor:

        for i in range(32):
            if divisor * (1 << i) > dividend:
                break

        dividend -= divisor * (1 << i - 1)



        result += (1 << i - 1)

    if not sign:
        result = -result

    if result > (1 << 31) - 1:
        return (1 << 31) - 1

    return result


dividend = 7
divisor = -3

print(divide(dividend, divisor))
