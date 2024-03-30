from linkedlist import *

''' Solution 1 : The idea is to reach the last node of the linked list using recursion then start
 reversing the linked list.'''


def reverse_recursive(head):
    if head is None or head.next is None:
        return head

    rest_head = reverse_recursive(head.next)  # this is the last node that will be new head

    rest_tail = head.next  # this is the node next to current head position as we need this to reverse the link
    rest_tail.next = head  # here we reverse the link by making rest_tail.next to head of current recursive call
    head.next = None  # this is the last node of the current recursive call, hence it's next must point to None

    return rest_head


'''Solution 2 : Idea is we're first going to reverse the current list and then we're going to recursively call for 
the remaining list.'''


def reverse_recursive_2(curr, prev=None):
    if curr is None:  # base condition to understand we have reached the end of LL , i.e. passed the last node
        return prev  # return the last node of the LL( means head in case of reversed LL)

    next = curr.next  # get the next node from curr, which will be new curr for the recursion
    curr.next = prev  # the prev now moves to next node which is curr

    return reverse_recursive_2(next, curr)  # call the recursion with new curr and prev


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
