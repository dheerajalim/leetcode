"""
Keep on dividing by 2 until the number is 1 and store the remainder.
the remainder in reverse order is the binary
"""


def decimal_to_binary(num):
    binary = ""
    # iterate until the number is not equal to 1
    while num != 1:
        # if the remainder to binary string
        if num % 2 == 1:
            binary += "1"
        elif num % 2 == 0:
            binary += "0"

        # keep on reducing the num , as we need binary
        # hence we divide by 2
        num = num // 2

    # since the last item is 1, and its binary is 1, hence we add 1
    binary += "1"
    # the result is reverse order of the way we added the 0 and 1 to binary string
    # hence we reverse the binary string
    return "".join(reversed(binary))


num = 13
result = decimal_to_binary(num)
print(result)
