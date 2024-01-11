"""https://leetcode.com/problems/time-needed-to-buy-tickets/"""
def time_to_buy(tickets, k):

    # the target index value
    target_person_tickets = tickets[k]
    # initiating the total time to be taken
    total_time = 0
    for i in range(len(tickets)):
        # condition if the tickets before k index are greater than k index
        # then count them target_person_tickets time
        if tickets[i] >= target_person_tickets and i < k:
            total_time += target_person_tickets
        # condition if the tickets after k index are greater than k index
        # then count them target_person_tickets - 1 times; since
        # the target_person_tickets will become 0 before them
        elif tickets[i] >= target_person_tickets and i > k:
            total_time += target_person_tickets - 1
        # this is for the target index to be included
        # as we have to make this 0
        elif i == k:
            total_time += target_person_tickets

        # base condition to consider all persons with less
        # count of tickets than target_person_tickets
        elif tickets[i] < target_person_tickets:
            total_time += tickets[i]

    return total_time


tickets = [5,2,3,8,2,1,6] #2
tickets = [2,3,4,2,1,3] #1
tickets = [3,3,2] #1
tickets = [5,1,1,1] #0

print(time_to_buy(tickets,0))
