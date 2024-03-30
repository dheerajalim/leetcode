"""
From the given list , find the number which appears odd times

Remember XOR with 0 is the same number, hence when here we do XOR of result and i
for the first element it will be XOR (0 ^ arr[0]), which will be arr[0].

The XOR is associative operator X ^ Y ^ Z == Y ^ X ^ Z == Z ^ Y ^ X

Hence when we do the XOR of the input array we always get the odd count number as output
"""


def find_odd(arr):
    res = 0
    for i in arr:
        res = i ^ res

    return res


arr = [10, 20, 20, 30, 30, 50]

print(find_odd(arr))
