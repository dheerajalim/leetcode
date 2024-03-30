from linkedlist import *


def remove_nth_end(head, n):
    if head is None:
        return None

    # if there is only one element then we just return None
    # as we need to remove head, and also question mention n >= 1
    if head.next is None:
        return None

    # maintain two pointers
    prev, curr = head, head

    # we move the curr pointer n times
    # this means the gap between prev and curr is n now,
    # so when we reach at the last node , then prev will point to
    # a node , just before the node to be deleted
    for i in range(n):
        # curr point to node at n distance
        curr = curr.next
        # if the curr crosses the limit , this means given n from behind
        # if counted points to the first node, hence we update the head and return
        if curr is None:
            head = head.next
            return head

    # now we keep on moving the prev and curr by 1 unit
    # if the curr.next is none, this means our prev is pointing to node
    # just before the target node
    while curr and curr.next:
        prev = prev.next
        curr = curr.next

    # we just update prev next to its next's next
    # this way target node is removed from liked list
    prev.next = prev.next.next

    # return the head
    return head


arr = [1, 2, 3, 4, 5]
head = create_linked_list(arr)
print_linked_list(head)
head = remove_nth_end(head, 3)
print_linked_list(head)
