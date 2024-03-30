from linkedlist import *


def maximum(head):
    if head is None:
        return None

    curr = head
    max_item = curr.data  # updating the max value to curr node value

    # iterating till the curr.next is available
    while curr.next:
        # if the current max is less than the next node value
        # then update the max to next node value
        if max_item < curr.next.data:
            max_item = curr.next.data
        curr = curr.next  # update curr to next node for iteration

    return max_item


def minimum(head):
    if head is None:
        return None
    curr = head
    min_item = curr.data

    while curr.next:
        # if the current min is greater than the next node value
        # then update the min to next node value
        if min_item > curr.next.data:
            min_item = curr.next.data

        curr = curr.next

    return min_item


arr = [1, 2, 3, 4, 5, 10, 4]
head = create_linked_list(arr)
print_linked_list(head)
print('Find Min')
print(minimum(head))

print('Find Max')
print(maximum(head))
