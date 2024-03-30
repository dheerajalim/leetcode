from linkedlist import *


def delete_last_node(head):

    # For the empty LL or if it only conatins the head
    if head is None or head.next is None:
        return None

    temp_head = head
    # Move till the second last element of the LL
    while temp_head.next.next is not None:
        temp_head = temp_head.next # Keep on updating the temp head to move inside the LL

    # Once we reach the second last element, we point it's next to None
    temp_head.next = None

    return head


arr = [1, 2, 3, 4]

print('==== Delete Last Node =====')
head = create_linked_list(arr)
print_linked_list(head)

head = delete_last_node(head)
print_linked_list(head)


