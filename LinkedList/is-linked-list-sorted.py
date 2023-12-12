from linkedlist import *


def increasing_order(curr):
    while curr.next:
        if curr.data > curr.next.data:
            return 0
        curr = curr.next

    return 1


def decreasing_order(curr):
    while curr.next:
        if curr.data < curr.next.data:
            return 0
        curr = curr.next

    return 1


def is_sorted(head):
    # Case 1 : for empty list or single node we assume it is sorted
    if head is None or head.next is None:
        return 1

    # Case 2 : Identifying the first non-repeating node
    curr = head

    while curr.next and curr.data == curr.next.data:
        curr = curr.next  # reaches at the first non-repeating node

    # Case 3:  If we reached the last node , that is the list has repeating elements
    if curr.next is None:
        return 1

    # Case 4 : Check if it is increasing order or decreasing order sorted
    if curr.data < curr.next.data:
        return increasing_order(curr.next)

    elif curr.data > curr.next.data:
        return decreasing_order(curr.next)


arr = [1, 2, 3, 4, 5, 10, 4]
head = create_linked_list(arr)
print_linked_list(head)
print('Is Sorted Linked List')
print(is_sorted(head))
