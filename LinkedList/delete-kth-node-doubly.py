from doubly_linked_list import *


# This is indexing with 1, and not 0

def delete_at_position(head, pos):
    # base condition for single or no node
    if head is None or head.next is None:
        return None

    # for invalid position
    if pos < 1:
        return head

    # Case 1: deleting the first node , requires updating the head
    if pos == 1:
        new_head = head.next
        head.next = None
        new_head.prev = None
        return new_head

    curr_pos = 1
    curr = head

    # iterating until we reach the node to be deleted
    while curr_pos != pos:
        curr = curr.next
        curr_pos += 1
        if curr is None:  # for pos > LL length this is required to be handled
            return head

    # reference to the new next node
    new_next = curr.next
    # Getting the prev node form curr position who will point to new next
    prev_node = curr.prev
    prev_node.next = new_next
    # This condition is required if we deleted the last node, to avoid None.prev
    if new_next: new_next.prev = prev_node
    # removing the prev and next reference of the curr node
    curr.prev, curr.next = None, None

    return head


print('Deleting from kth position of a doubly Linked List')
arr = [1, 4, 5, 9, 2]
head = create_doubly_linked_list(arr)
print_linked_list(head)
head = delete_at_position(head, 1)
print_linked_list(head)
