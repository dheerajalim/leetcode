"""Merging two sorted linked lists"""


def merge_ll(head1, head2):

    # In case one or both of the LL are empty
    if head1 is None and head2 is None:
        return None

    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # now we'll get the starting point for the merged LL, the new head

    if head1.data < head2.data:
        final_head = head1
        final_tail = head1
        head1 = head1.next

    else:
        final_head = head2
        final_tail = head2
        head2 = head2.next

    while head1 is not None and head2 is not None:

        if head1.data < head2.data:

            final_tail.next = head1
            final_tail = head1
            head1 = head1.next
        else:
            final_tail.next = head2
            final_tail = head2
            head2 = head2.next

    if head1 is None:
        final_tail.next = head2
    elif head2 is None:
        final_tail.next = head1

    return final_head
