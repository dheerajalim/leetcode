from doubly_linked_list import *


def insert(head, data):
    new_node = Node(data)

    # For an empty linked list
    if head is None:
        return new_node

    # if the new node is smaller than head, we create a new head
    if data < head.data:
        head.prev = new_node
        new_node.next = head
        return new_node
    curr = head
    # iterating till we reach a node that is greater than new node data
    while curr and curr.data <= data:
        prev = curr  # keeping reference of prev node
        curr = curr.next  # updating curr pointer
        if curr is None:  # to handle insertion after last node
            # here is the use of new prev node
            prev.next = new_node
            new_node.prev = prev
            return head

    # otherwise , keeping the prev of curr node reference
    prev_curr = curr.prev

    # setting the links for new node prev and next
    new_node.prev, new_node.next = prev_curr, curr

    # updating the prev and curr nodes links towards new node
    prev_curr.next, curr.prev = new_node, new_node

    return head


print('Insert into sorted DLL')
arr = [1, 3, 4, 5, 6]
head = create_doubly_linked_list(arr)
print_linked_list(head)
head = insert(head, 0)
print_linked_list(head)
