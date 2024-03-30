"""
The steps to follow the fractional knapsack is to maximize the value of the sack with the given capacity of the sack

//Ab bhai agar maximum value pata karni hai based on weight to hum 1 unit me kittni value hai wo nikal lenge
usase samaj aa jyega ki kausa pair maximum value generate krta hai per unit of weight ke

and jo sabse zada vcalue genertae krta hai usko pehle le lenge as this is the idea, we want to maximize the value//


Since this question ask to maximize the value within the given sack weight, we use greedy approach

Steps:
1. Get the value/weight
2. Sort these in the descending order
3. Now iterate over these sorted items and check if their weight is less the available sack weight
    if yes : then completely add the value to the knapsack
    else: Add th efraction of the value in the sack
4. The fraction value is calculated = required_weight *(value per unit weight)

"""


def fractional_knapsack(n, w, arr):
    """

    :param n: Total number of items
    :param w: Knapsack capacity
    :param arr: [value, weight]
    :return: Maximum total value for the given knapsack
    """

    # get the value/weight ratio and sort them in descending order

    value_by_weight = sorted(arr, key=lambda x: x[0] / x[1], reverse=True)

    # iterate over the value by weight ratio
    # keep on checking if the weight can be accommodated totally or partially

    remaining_weight = w
    total_value = 0

    # now we iterate over the sorted list of value / weight
    for value, weight in value_by_weight:
        # if the weight is <= knapsack capacity
        # we take the complete value
        if weight <= remaining_weight:
            total_value += value
            remaining_weight -= weight
        # else if the knapsack weight is less than the current available weight
        # we can take the partial weight and add the value of the partial weight
        # if we reach here we are sure that the knapsack is full now
        # ,so we return
        else:
            total_value += remaining_weight * (value / weight)
            return total_value

    return total_value


n = 3
w = 70
arr = [[600, 50], [500, 20], [400, 30]]

print(fractional_knapsack(n, w, arr))
