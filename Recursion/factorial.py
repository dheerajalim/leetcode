def factorail(n):

    if n == 0 :
        return 1

    return n * factorail(n-1)


print(factorail(3))