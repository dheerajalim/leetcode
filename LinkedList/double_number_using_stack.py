"""
https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/?envType=daily-question&envId=2024-05-07
"""
from linkedlist import *


def double_it(head):
    stack = []

    # traverse the linked list and add items to the stack
    while head:
        stack.append(head.data)
        head = head.next

    curr = None

    carry = 0
    while stack:
        item = stack.pop()

        # double the item
        item = item * 2
        item += carry
        # the mod is the node value
        mod = item % 10

        # creating a new node
        node = Node(mod)
        node.next = curr
        curr = node

        # the division is the value to be added to next node
        carry = item // 10

    if carry:
        node = Node(carry)
        node.next = curr
        curr = node

    return curr


head = [1,1,1]
head = create_linked_list(head)
head = double_it(head)
print_linked_list(head)
