from circular_linked_list import *


def delete_head(head):
    # Case 1 : when the LL is empty
    if head is None:
        return None

    # Case 2 : When there is only a single node
    if head.next == head:
        return None

    # Case 3 : Deleting the head in a LL
    """
    Copying the head.next data to head.data so that the head.next can be deleted
    Now updating the head.next to the head.next.next, making head.next disappear from LL
    """
    new_next = head.next.next
    head.data = head.next.data
    head.next = new_next

    return head


arr = [1, 2, 3, 4, 5]

print('Constant time Deletion at end')
head = create_circular_linked_list(arr)
print_linked_list(head)
head = delete_head(head)
print_linked_list(head)
