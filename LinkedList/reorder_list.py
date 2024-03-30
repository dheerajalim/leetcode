"""
https://leetcode.com/problems/reorder-list/description/?envType=daily-question&envId=2024-03-23
"""

from linkedlist import *


def reorder_list(head):
    if head.next is None:
        return head
    slow, fast = head, head

    # finding the mid of the linked list

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # the next of slow is the head of the second part of
    # the linked list after middle node
    new_head = slow.next
    # this is used to set the last node of the first part of
    # linked list to point to None
    slow.next = None

    # reverse the second part of the ll
    prev = None
    while new_head:
        next_node = new_head.next
        new_head.next = prev
        prev = new_head
        new_head = next_node

    # prev is the head of second part

    curr = head
    # now iterate over the first part of the linked list
    # and insert the nodes in between two nodes from second part of linked list
    # to the first part
    while curr and prev:
        next_node_a = curr.next
        curr.next = prev
        next_node_b = prev.next
        prev.next = next_node_a
        prev = next_node_b
        curr = next_node_a

    return head


arr = [1, 2, 3, 4, 5, 6, 7, 8]
# arr = [1, 2, 3, 4]

head = create_linked_list(arr)
print_linked_list(head)

head = reorder_list(head)
print_linked_list(head)
