"""
Alice has some number of cards and she wants to rearrange the
cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card
and an integer groupSize, return true if she can rearrange the cards, or false otherwise.



Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
"""
import heapq
from collections import deque


def count_cards(hand):
    # get the count of all the cards
    count = {}
    for card in hand:
        count[card] = 1 + count.get(card,0)

    return count


def is_straight_hands(hand, size):
    # if the size is not valid to make
    # given size group return false
    if len(hand) % size != 0:
        return False

    # get all the cards from cards_count
    value_count = count_cards(hand)
    minH = list(value_count.keys())
    # create a minheap
    heapq.heapify(minH)
    # iterate until heap is not empty
    while minH:
        # get the min element from the heap
        first = minH[0]
        # then check if the consecutive elements
        # until given size are present in hash map
        for i in range(first, first+size):
            # if not in hash map, return false
            if not value_count.get(i):
                return False
            # reduce the count of the element from
            # hash map
            value_count[i] -= 1

            # if the element in hash map becomes 0 count
            # then this needs to be the min element in heap
            if value_count[i] == 0:
                # if not the min, then return false
                if i != minH[0]:
                    return False
                # pop the min element
                # as this is now having 0 count
                heapq.heappop(minH)

    return True


hand = [1,2,3,6,2,3,4,7,8]
hand = [1,1,2,2,3,3]
hand = [34,80,89,15,38,69,19,17,97,98,26,77,8,31,79,70,103,3,13,21,81,53,33,14,60,68,33,59,84,23,97,90,76,82,66,83,23,22,16,18,98,25,16,61,84,100,4,68,101,25,23,9,10,55,2,67,39,52,102,99,40,11,83,24,81,53,96,23,13,24,99,67,22,51,31,58,78,88,5,15,24,32,81,91,96,16,54,22,56,69,14,82,32,34,83,24,37,82,54,21]


group_size = 4

print(is_straight_hands(hand, group_size))
