from linkedlist import *


def deleteMiddle(head):
    # Case 1 : If the LL is empty
    if head is None:
        return None
    # Case 2 : For only single node presence
    if head.next is None:
        return None

    # Using 2 pointer approach
    slow_ptr = head
    fast_ptr = head

    # reaching the middle of the LL
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    # This condition handles the scenario with only two nodes in LL
    if slow_ptr.next is None:
        head.next = None
        return head

    # Delete's the middle node
    slow_ptr.data = slow_ptr.next.data
    slow_ptr.next = slow_ptr.next.next

    return head


arr = [1, 2, 3, 4, 5]

print('Delete from Middle')
head = create_linked_list(arr)
print_linked_list(head)
head = deleteMiddle(head)
print_linked_list(head)