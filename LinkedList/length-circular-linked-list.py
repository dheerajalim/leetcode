from circular_linked_list import *


def length_cll(head):
    if head is None:
        return 0

    if head.next == head:
        return 1

    curr = head.next
    length = 1
    while curr != head:
        length += 1
        curr = curr.next

    return length


arr = [1, 2, 3, 4, 5]

print('Delete from Middle')
head = create_circular_linked_list(arr)
print_linked_list(head)
print(length_cll(head))

