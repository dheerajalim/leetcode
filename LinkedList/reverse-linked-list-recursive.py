from linkedlist import *


def reverse_recursive(head):

    if head is None or head.next is None:
        return head

    rest_head = reverse_recursive(head.next)

    rest_tail = head.next
    rest_tail.next = head
    head.next = None

    return rest_head


arr = [10, 20, 30, 40, 50]
head = create_linked_list(arr)
print_linked_list(head)
print('Reversed Linked List')
head = reverse_recursive(head)
print_linked_list(head)
