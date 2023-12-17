from doubly_linked_list import *


def delete_last_node(head):
    # Base conditions
    if head is None:
        return None

    if head.next is None and head.prev is None:
        return None

    curr = head

    # Iterating to reach the last node of the LL
    while curr.next:
        curr = curr.next

    # fetching the prev node from the last node
    curr_prev = curr.prev
    # Updating the prev of last Node to None as this node needs to be deleted
    curr.prev = None
    # Now updating the next of second last node to None to technically delete last Node
    curr_prev.next = None

    return head


arr = [1, 2, 3, 4, 5]

print('Delete Last Node of DLL')
head = create_doubly_linked_list(arr)
print_linked_list(head)
head = delete_last_node(head)
print_linked_list(head)
