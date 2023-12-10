from linkedlist import *


def remove_duplicate(head):
    curr = head  # initializing the head to curr

    # iteration inside LL unitl curr is valid
    while curr is not None and curr.next is not None:
        # if a duplicate is found , deleted that node and point the next of curr to curr.next.next
        if curr.data == curr.next.data:
            curr.next = curr.next.next

        # Note this condition, we will only update this if there is no duplicate left
        else:
            curr = curr.next


def remove_duplicate_two_pointer(head):
    if head is None or head.next is None:
        return head

    first_ptr = head  # Points to the head
    second_ptr = head.next  # points to the next of head

    # keep on moving the second pointer until a node is there
    while second_ptr and second_ptr.next:
        if first_ptr.data == second_ptr.data:  # if the duplicate is present , move the second ptr
            second_ptr = second_ptr.next
        else:
            # otherwise point the next for first ptr to the second ptr(this deletes the duplicate nodes)
            # update the first ptr to its new next and second ptr to the next pointer
            first_ptr.next = second_ptr
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next

        first_ptr.next = second_ptr  # this condition is to update the frst pointer to the lates second ptr


arr = [10, 20, 20, 30, 30, 30, 40]
head = create_linked_list(arr)
print_linked_list(head)

print("remove duplicates")
remove_duplicate(head)
print_linked_list(head)

print("Two Pointer approach")
remove_duplicate_two_pointer(head)
print_linked_list(head)
