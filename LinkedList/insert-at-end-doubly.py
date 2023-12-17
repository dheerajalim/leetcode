from doubly_linked_list import *


def insert_at_end(head, data):
    # Case 1 : Create a new node in case of empty linked list
    if head is None:
        return Node(data)

    curr = head
    # Iterate till the last node
    while curr.next:
        curr = curr.next

    # Creating a new node
    new_node = Node(data)
    # updating the curr.next to new node
    curr.next = new_node
    # udpating new nodes prev to curr node , which is last node
    new_node.prev = curr

    return head


arr = [1, 2, 3, 4, 5]

print('Insert at End of DLL')
head = create_doubly_linked_list(arr)
print_linked_list(head)
head = insert_at_end(head, 10)
print_linked_list(head)
