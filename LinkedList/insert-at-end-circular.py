from circular_linked_list import *


def insert_at_end_constant(head, node):
    # Case 1 : if head is None, we insert the new node and return
    if head is None:
        new_node = Node(node)
        new_node.next = new_node
        return new_node

    curr = head  # refer to the head
    new_node = Node(curr.data)  # create a new node with curr data(which is head)
    new_next = curr.next  # refer the curr.next as new next to store it
    curr.data = node  # now update the curr.data with new data(which is head)
    curr.next = new_node  # point curr.next to new_node(which contains old head value)
    new_node.next = new_next  # point new_node to the new_next to create link

    # note:we return the new_node as this is basically head.next, to show node is inserted at end
    return new_node


arr = [1, 2, 3, 4, 5]

print('Constant time insertion at end')
head = create_circular_linked_list(arr)
print_linked_list(head)
head = insert_at_end_constant(head, 10)
print_linked_list(head)
