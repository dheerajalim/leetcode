# Assuming K starts from 1
from circular_linked_list import *


def delete_node_head(head):
    head.data = head.next.data
    head.next = head.next.next
    return head


def delete_kth_node(head, k):
    # Case 0 :
    if k == 0:
        return head

    # Case 1 : Empty LL
    if head is None:
        return None

    # Case 2 : Single node present
    if head.next == head:
        return None

    # Case 3 : To delete head node
    if k == 1:
        return delete_node_head(head)

    # Case 4 : To delete Node at kth position
    """
    We will iterate till a node one position before kth node
    This will help us to point this k-1 th node to the kth's next node
    This way kth node can be skipped
    """
    curr = head
    for _ in range(k - 2):
        curr = curr.next
        if curr.next == head:  # To handle condition where k > length of LL
            return

    curr.next = curr.next.next
    return head


arr = [1, 2, 3, 4, 5]

print('Constant time Deletion at end')
head = create_circular_linked_list(arr)
print_linked_list(head)
head = delete_kth_node(head, 2)
print_linked_list(head)
