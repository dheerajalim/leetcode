def middle_linked_list(head):

    if head is None or head.next is None:
        return head

    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None or fast_ptr.next is not None:

        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr
