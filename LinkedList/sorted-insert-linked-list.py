# Insert a new node inside a sorted linked list at the correct position

from linkedlist import *


def insert_sorted(head, node):

    # Case 1 : When the Linked List is empty
    if head is None:
        return Node(node)

    # Case 2: When the node to be inserted is smaller than the head

    if node <= head.data:
        new_head = Node(node)
        new_head.next = head
        return new_head

    # Case 3 : When the item to be inserted is the in between
    temp_head = head
    while temp_head.next is not None:

        current_data = temp_head.data
        next_data = temp_head.next.data

        if current_data <= node <= next_data:
            new_node = Node(node)
            new_next = temp_head.next
            temp_head.next = new_node
            new_node.next = new_next
            return head

        temp_head = temp_head.next

    # Case 4 : When the new node needs to be inserted at the end
    # currently if we reach here, that means we are at the last node of the LL
    if temp_head.data <= node:
        temp_head.next = Node(node)

    return head


# SOLUTION 2:

def insert_sorted(head, node):
    # Case 1 : When the Linked List is empty
    if head is None:
        return Node(node)

    # Case 2: When the node to be inserted is smaller than the head

    if node <= head.data:
        new_head = Node(node)
        new_head.next = head
        return new_head

    # Case 3 : When the item to be inserted is not at the beginning
    temp_head = head
    new_node = Node(node)
    while temp_head.next is not None and temp_head.next.data < node:
        temp_head = temp_head.next

    # In case of last node, this points to None, otherwise to the next node of the temp_head
    new_node.next = temp_head.next
    temp_head.next = new_node  # the temp_head points to the new node created

    return head


arr = [10, 20, 30, 40, 50]

print('==== Insert Node inside a sorted LL =====')
head = create_linked_list(arr)
print_linked_list(head)

head = insert_sorted(head, 45)
print_linked_list(head)
