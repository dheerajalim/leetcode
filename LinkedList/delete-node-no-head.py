# You are given the node to be deleted node. You will not be given access to the first node of head.
# All the values of the linked list are unique, and it is guaranteed that the given node is not the last node in the linked list.

from linkedlist import *


def delete_node(node):

    node.data = node.next.data
    node.next = node.next.next

    return


arr = [1, 2, 3, 4]

print('==== Delete Node =====')
head = create_linked_list(arr)
print_linked_list(head)

delete_node(head.next.next)
print_linked_list(head)
