from linkedlist import *


def sumOfElements(head):
    # code here
    if head is None:
        return None

    sum = 0

    curr = head

    while curr:
        sum += curr.data  # keep on adding the current node data
        curr = curr.next  # update the current node to next node

    return sum


arr = [10, 20, 30, 40, 50]
head = create_linked_list(arr)
print_linked_list(head)
print('Sum of Linked List')
print(sumOfElements(head))
