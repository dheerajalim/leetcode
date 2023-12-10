from linkedlist import *


def reverse_iterative(head):
    if head is None or head.next is None:
        return head

    prev = None
    curr = head

    while curr is not None:
        new_curr = curr.next
        curr.next = prev
        prev = curr
        curr = new_curr

    return prev


arr = [10, 20, 30, 40, 50]
head = create_linked_list(arr)
print_linked_list(head)
print('Reversed Linked List')
head = reverse_iterative(head)
print_linked_list(head)
