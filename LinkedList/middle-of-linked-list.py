from linkedlist import *


def middle_node(head):
    # condition if the LL is empty
    if head is None:
        return None

    # condition if there is single node in LL
    if head.next is None:
        return head.data

    slow_ptr, fast_ptr = head, head

    # Iterating until we hot the condition of fast ptr being None or its next being None
    while fast_ptr is not None and fast_ptr.next is not None:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
    # the slow ptr position is our result
    return slow_ptr.data


arr = [1, 2, 3, 4, 5]
head = create_linked_list(arr)

print(middle_node(head))
