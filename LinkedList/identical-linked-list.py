from linkedlist import *


def identical(head1, head2):
    if head1 is None and head2 is None:
        return True
    # initializing to the head
    curr1, curr2 = head1, head2

    while curr1 and curr2:
        # if both LL have same node value, then move to next node
        if curr1.data == curr2.data:
            curr1, curr2 = curr1.next, curr2.next
        else:
            return False
    # if any LL is still having nodes, this means length mismatch
    if curr1 or curr2:
        return False

    return True


arr1 = [1, 2, 3, 4, 5, 10, 4]
arr2 = [1, 2, 3, 4, 5, 10, 5]
head1 = create_linked_list(arr1)
print_linked_list(head1)
head2 = create_linked_list(arr2)
print_linked_list(head2)
print('Is identical')
print(identical(head1, head2))
