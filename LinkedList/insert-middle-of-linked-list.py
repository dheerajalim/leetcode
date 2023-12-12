"""
Given a linked list of size N and a key. The task is to insert the key in the middle of the linked list.

Example 1:

Input:
LinkedList = 1->2->4
key = 3
Output: 1 2 3 4
Explanation: The new element is inserted
after the current middle element in the
linked list.
"""

from linkedlist import *


def insert_at_middle(head, node):
    # Case 1 , if the LL is empty, we return the new Node
    if head is None:
        return Node(node)

    new_node = Node(node)

    # Keeping both pointers at head
    # Another possible way is to keep slow at head and fast at head.next: then the iteration can be as similar
    # to finding the middle of LL
    slow_ptr = head
    fast_ptr = head

    while fast_ptr.next and fast_ptr.next.next:  # Move the pointers
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    new_node.next = slow_ptr.next  # update the next of new node to slows next
    slow_ptr.next = new_node  # update slow's next to new node

    return head


arr = [10]
head = create_linked_list(arr)
print_linked_list(head)
print('Insert in middle Linked List')
head = insert_at_middle(head, 100)
print_linked_list(head)
