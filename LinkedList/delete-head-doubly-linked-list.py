from doubly_linked_list import *


def delete_head(head):
    # Base conditions
    if head is None:
        return None

    if head.next is None and head.prev is None:
        return None

    # updating the head to the next of head node and updating prev to None
    new_head = head.next
    new_head.prev = None
    return new_head


arr = [1, 2, 3, 4, 5]

print('Delete head of DLL')
head = create_doubly_linked_list(arr)
print_linked_list(head)
head = delete_head(head)
print_linked_list(head)
