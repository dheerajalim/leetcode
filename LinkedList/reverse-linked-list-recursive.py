from linkedlist import *


''' Solution 1 : The idea is to reach the last node of the linked list using recursion then start
 reversing the linked list.'''


def reverse_recursive(head):

    if head is None or head.next is None:
        return head

    rest_head = reverse_recursive(head.next)

    rest_tail = head.next
    rest_tail.next = head
    head.next = None

    return rest_head


'''Solution 2 : Idea is we're first going to reverse the current list and then we're going to recursively call for 
the remaining list.'''


def reverse_recursive_2(curr, prev = None):

    if curr is None:
        return prev

    next = curr.next
    curr.next = prev

    return reverse_recursive_2(next, curr)


arr = [10, 20, 30, 40, 50]
head = create_linked_list(arr)
print_linked_list(head)
print('Reversed Linked List')
head = reverse_recursive(head)
print_linked_list(head)

print('Reversed Linked List Solution 2')
arr = [10, 20, 30, 40, 50]
head = create_linked_list(arr)
head = reverse_recursive_2(head)
print_linked_list(head)