"""
https://leetcode.com/problems/palindrome-linked-list/description/?envType=daily-question&envId=2024-03-22
"""

from linkedlist import *


def palindrome_ll(head):
    # get the middle of the LL and reverse the first part
    slow, fast = head, head
    prev = None
    while fast and fast.next:
        fast = fast.next.next

        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    if fast:
        slow = slow.next

    while prev and slow:
        if prev.data != slow.data:
            return False

        prev, slow = prev.next, slow.next

    return True


arr = [1, 2, 3, 2, 1]
head = create_linked_list(arr)
print_linked_list(head)
print(palindrome_ll(head))
