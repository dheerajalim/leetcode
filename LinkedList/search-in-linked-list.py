from linkedlist import *


# Return 1 , if found , else 0
def searchLinkedList(head, x):
    # Condition if the Linked List is empty
    if head is None:
        return 0

    curr = head  # keeping the temp head

    while curr:
        if curr.data == x:  # in case match is found we return 1
            return 1
        curr = curr.next  # for the iteration to move to next node

    return 0


arr = [10, 20, 30, 40, 50]
head = create_linked_list(arr)
print_linked_list(head)
print('Search Linked List')
print(searchLinkedList(head, 30))
