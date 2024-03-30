from doubly_linked_list import *


def insert_at_beginning(head, data):
    # Case 1 : For empty LL , add new node
    if head is None:
        return Node(data)

    new_node = Node(data)

    # Update the next of new node to head
    new_node.next = head
    # Update the prev of old head to new head
    head.prev = new_node
    return new_node


arr = [1, 2, 3, 4, 5]

print('Insert at beginning of DLL')
head = create_doubly_linked_list(arr)
print_linked_list(head)
head = insert_at_beginning(head, 10)
print_linked_list(head)

