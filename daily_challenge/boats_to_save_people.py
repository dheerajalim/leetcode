"""
https://leetcode.com/problems/boats-to-save-people/?envType=daily-question&envId=2024-05-04

The idea is to accommodate the max weighted person first along with the greedy approach of minimizing
the boats, so try to accommodate the least weighted person with heavyweight person

Note: We can only send max 2 people in a boat
"""


def rescue_boats(people, limit):
    people = sorted(people, reverse=True)

    start, end = 0, len(people) - 1

    count = 0

    while start <= end:
        # try to accommodate max weight and least weight
        if people[start] + people[end] <= limit:
            count += 1
            start += 1
            end -= 1

        # else if oly the max weight person can go, then send him
        elif people[start] <= limit:
            count += 1
            start += 1

        # otherwise try to mail two least weight people and send together
        elif people[end] + people[end - 1] <= limit:
            end -= 2

        # if only the least weight person is close to the boat limit, then send him alone
        elif people[end] <= limit:
            end -= 1

    return count


people = [1, 2]
limit = 3

# people = [3,2,2,1]
# limit = 3

# people = [1]
# limit = 5

people = [5, 4, 3, 1]
limit = 4

print(rescue_boats(people, limit))
