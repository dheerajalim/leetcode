"""
https://leetcode.com/problems/reveal-cards-in-increasing-order/description/?envType=daily-question&envId=2024-04-10
"""

from collections import deque


def deck_reveal(deck):
    # sort the deck in decreasing order

    deck = sorted(deck, reverse=True)

    dq = deque()

    for card in deck:

        if len(dq) >= 2:
            last_card = dq.pop()
            dq.appendleft(last_card)

            dq.appendleft(card)

        else:
            dq.appendleft(card)

    return list(dq)


deck = [17, 13, 11, 2, 3, 5, 7]
deck = [1, 1000]

print(deck_reveal(deck))
