"""https://leetcode.com/problems/time-needed-to-buy-tickets/description/?envType=daily-question&envId=2024-04-09"""


def time_required(tickets, k):
    """
    Everyone before the k person will take same time as kth person to buy tickets
    so the  kth person turn can come
    Every person after kth person if has less requirement then kth person will take time equal to tickets
    else it will take 1 unit of time less than kth person as kth person will get free a second before
    all  the people behind him
    """
    total_time = 0
    for i, ticket in enumerate(tickets):

        # for all the people before the kth person and kth person also
        if i <= k:
            # if the ticket is less than or equal to kth person
            # then they both will take time equal to tickets they have
            if ticket <= tickets[k]:
                total_time += ticket
            # if the tickets is more than the kth person
            # then they will take max kth person time , because kth person will get free before them
            else:
                total_time += tickets[k]
        # for all the people after kth person
        else:
            # if they have less tickets than kth person, then they will get free first
            # hence time taken by them will be equal to the tickets they have
            if ticket < tickets[k]:
                total_time += ticket
            # otherwise if they have more tickets than kth person , then kth person
            # will get free before them and these people will be able to buy 1 ticket
            # less than kth person hence their time is ticket[k] - 1
            else:
                total_time += tickets[k] - 1

    return total_time


tickets = [2, 3, 2]
k = 2
tickets = [5, 1, 1, 1]
k = 0
print(time_required(tickets, k))
