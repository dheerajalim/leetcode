from linkedlist import *


def nth_node_from_end(head, n):
    # Case , where the LL is empty
    if head is None:
        return None
    if n <= 0:  # In case the requested node is 0 or negative, we expect the n >=1
        return None
    # finding the length of the LL

    temp_head = head
    length = 0
    while temp_head is not None:
        temp_head = temp_head.next
        length += 1

    if length < n:
        return None
    # the nth node from last would be the (length -n + 1) from beginning

    node_from_beginning = length - n + 1
    nth_node = head
    for i in range(1, node_from_beginning):
        nth_node = nth_node.next

    return nth_node.data


# Solution 2 : Using two pointer approach

def nth_node_from_end_twopointer(head, n):
    # Case 1 , when the LL is empty
    if head is None:
        return None

    # Case 2 : For n <=0 we return None, we expect n >= 1 as the count of node is starting with 1
    if n <= 0:
        return None

    first_ptr = head
    second_ptr = head

    # Moving the first_ptr to nth nodes
    for i in range(n):

        if first_ptr is None: # this condition would be required to see if the first_ptr has moved ahead the last node, which means
            return None       # the requested nth node from end is greater than the length of LL

        first_ptr = first_ptr.next  # keep moving the first ptr

    # Now move the first and second ptr one node at a time if the first ptr is still inside the Length of LL
    while first_ptr:
        second_ptr = second_ptr.next
        first_ptr = first_ptr.next

    return second_ptr.data  # return the data of slow ptr


arr = [1, 2, 3, 4, 5]
head = create_linked_list(arr)
n = 5
print(nth_node_from_end(head, n))
print(nth_node_from_end_twopointer(head, n))
