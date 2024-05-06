"""
https://leetcode.com/problems/remove-nodes-from-linked-list/description/?envType=daily-question&envId=2024-05-06
"""
from linkedlist import *


def remove_node(head):
    if head.next is None:
        return head
    # first iterate over the linked list and store the nodes in stack
    stack = []

    curr = head

    while curr:
        stack.append(curr)
        curr = curr.next

    # now pop the item from the stack and check if the next item is greater or not
    # pop the first item for comparison

    new_head = stack.pop()

    while stack:
        # get the last item from the satck
        last_item = stack.pop()
        # if last_item is greater than the new_head, then this means this is going to be the
        # new head, hence we update the next of last_item to the new_head and update new_head
        if last_item.data >= new_head.data:
            last_item.next = new_head
            new_head = last_item

    return new_head


arr = [5, 2, 13, 3, 8]
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
head = create_linked_list(arr)
print_linked_list(head)

new_head = remove_node(head)

print_linked_list(new_head)
