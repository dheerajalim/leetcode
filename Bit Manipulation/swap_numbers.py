def swap_numbers(a, b):
    # before
    print(f'a : {a} and b : {b}')

    # after
    a = a ^ b # this is a ^ b
    b = a ^ b # this becomes (a ^ b) ^ b ; where b^b is 0
    a = a ^ b # this becomes (a ^ b) ^ a ; since b = a from above step

    print(f'a : {a} and b : {b}')


a = 5
b = 10

swap_numbers(a, b)
