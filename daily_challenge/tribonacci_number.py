"""
https://leetcode.com/problems/n-th-tribonacci-number/description/?envType=daily-question&envId=2024-04-24
"""

"""
Doing this using Recursion gives TLE

But recursion code is 
def tribonacci(n):
    
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1


    return tribonacci(n-3) + tribonacci(n-2) + tribonacci(n-1)
"""
def tribonacci(n):
    store = [0, 1, 1]
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    # store the new item in list and the keep on appending this item
    # for the next item consider the last three items
    for i in range(3, n + 1):
        store.append(store[i - 3] + store[i - 2] + store[i - 1])

    return store[n]


n = 31
print(tribonacci(n))
