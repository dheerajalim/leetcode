"""
To remove the last set bit
"""


def remove_last_set(num):
    return num & (num - 1)


num = 13

print(remove_last_set(num))
