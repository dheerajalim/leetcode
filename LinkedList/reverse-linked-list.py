def reverse_ll(head):
    """Iterative approach"""
    if head is None or head.next is None:
        return head

    prev = None
    current_node = head

    while current_node is not None:

        next_node = current_node.next
        current_node.next = prev
        prev = current_node
        current_node = next_node

    return head


def reverse_ll(head):

    """Iterative approach"""

    if head is None or head.next is None:
        return head

    smallhead = reverse_ll(head.next)

    tail = head.next
    tail.next = head
    head.next = None


    return smallhead





