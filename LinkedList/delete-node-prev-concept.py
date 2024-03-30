# deleting node from the given position

from linkedlist import *


def delete_node(head, position):
    if head is None:  # for empty LL
        return head

    if position == 0:  # for handling the deletion at head
        return head.next

    prev = None
    curr = head
    curr_pos = 0

    while curr.next:  # till the second last node to allow deletion of last node as well
        curr_pos += 1  # updating the position with each iteration
        prev = curr  # setting the prev node
        curr = curr.next  # updating the curr node to next node

        if curr_pos == position:  # checking if we reached the required position
            prev.next = curr.next  # updating the prev.next to curr.next to avoid the node at required position
            return head

    return head


arr = [1, 2, 3, 4]
head = create_linked_list(arr)
print_linked_list(head)

print('==== Delete by Node Position=====')
head = delete_node(head, 2)
print_linked_list(head)
