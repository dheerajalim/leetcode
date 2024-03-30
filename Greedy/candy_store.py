"""
The idea is to sort the array based on prices, once ascending and once descending
This way for the min amount we start from the 0th index and keep on reducing the jth index which
points to the nth index, this makes sure that k candies are getting free in each iteration

Similarly for the max amount we sort the array ain descending order andfollow the same concept, where
the max amount is considered first and the smallest amount candies are made free
"""


def candyStore(candies, N, k):
    # find the max and min amount

    # to find the min amount sort in ascending order
    # to find the max amount sort in descending order
    min_candies = sorted(candies)
    max_candies = min_candies[::-1]

    # we keep two pointer, at the oth index and at the last index
    i = 0
    j = N - 1

    min_amount, max_amount = 0, 0
    # we iterate until we reach j does not cross i
    while i <= j:
        # in the nim_candies array, we take the min amount and
        # in the max_candies array, we take the max amount
        # reduce j by k values as these will be free now
        min_amount += min_candies[i]
        max_amount += max_candies[i]
        i += 1
        j = j - k

    return min_amount, max_amount


N = 5
K = 4
candies = [3, 2, 1, 4, 5]

candyStore(candies, N, K)
