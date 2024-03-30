from circular_linked_list import *


# Solution 1 : Linear Time O(N)
def insert_at_beginning(head, node):
    # Case 1 : if head is None, we insert the new node and return
    if head is None:
        new_node = Node(node)
        new_node.next = new_node
        return new_node

    # Case 2 : Insert at beginning, by updating the head
    # and reference of the last node to new head

    curr = head.next

    while curr.next != head:
        curr = curr.next

    new_node = Node(node)
    curr.next = new_node
    new_node.next = head

    return new_node


# Solution 2 : Constant Time O(1)

def insert_at_beginning_constant(head, node):
    # Case 1 : if head is None, we insert the new node and return
    if head is None:
        new_node = Node(node)
        new_node.next = new_node
        return new_node

    # Case 2 : Insert at beginning

    curr = head  # refer to the head
    new_next = curr.next  # refer the curr.next as new next to store it
    new_node = Node(curr.data)  # create a new node with curr data(which is head)
    curr.data = node  # now update the curr.data with new data(which is head)
    curr.next = new_node  # point curr.next to new_node(which contains old head value)
    new_node.next = new_next  # point new_node to the new_next to create link

    return head


arr = [1, 2, 3, 4, 5]

head = create_circular_linked_list(arr)

print_linked_list(head)

print('Linear time insertion')
head = insert_at_beginning(head, 10)
print_linked_list(head)

print('Constant time insertion')
head = create_circular_linked_list(arr)
head = insert_at_beginning(head, 10)
print_linked_list(head)
