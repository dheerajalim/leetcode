from doubly_linked_list import *


def addNode(head, p, data):
    # Code here

    new_node = Node(data)
    # Case 1 : for Invalid value of position
    if p < 0:
        return

    curr_pos = 0
    curr = head

    # Reaching till the node, after which the insertion of node is required
    while curr_pos != p:
        curr_pos += 1
        curr = curr.next
        # to handle condition when p > length of LL
        if curr is None:
            return

    # storing the new of curr to keep reference
    new_next = curr.next
    # this condition if for inserting new node after last node
    # Since if new_next is None, then it will not have prev
    if new_next is None:
        curr.next, new_node.prev = new_node, curr
    else:
        curr.next, new_node.prev = new_node, curr
        new_node.next, new_next.prev = new_next, new_node


arr = [1, 2, 3, 4, 5]

print('Insert at nth DLL')
head = create_doubly_linked_list(arr)
print_linked_list(head)
addNode(head, 2, 100)
print_linked_list(head)
