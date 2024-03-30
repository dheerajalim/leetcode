from doubly_linked_list import *


def reverse_doubly_linked_list(head):
    # Case 1 : When the head is None
    if head is None:
        return None
    # Case 2 : For a single node presence
    if head.next is None:
        return head

    # Setting up the curr to head and prev to None
    curr = head
    prev = None

    # Iterating till the end of the LL
    while curr:
        # Storing the prev of the LL to understand the new head of the reversed LL
        prev = curr
        # Swapping the Nodes by updating the prev and nex
        curr.prev, curr.next = curr.next, curr.prev
        # Since prev is new next , hence we update curr to curr.prev
        curr = curr.prev

    # When curr is None, that time prev is at the last node, which is our new head
    return prev


arr = [1, 2, 3, 4, 5]

print('Reverse DLL')
head = create_doubly_linked_list(arr)
print_linked_list(head)
head = reverse_doubly_linked_list(head)
print_linked_list(head)
