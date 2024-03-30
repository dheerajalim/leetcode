# Sun of first N natural numbers using recursion

def sum_numbers(n, sum):

    if n == 0:
        return sum

    sum += n

    return sum_numbers(n-1, sum)


print(sum_numbers(6, 0))
