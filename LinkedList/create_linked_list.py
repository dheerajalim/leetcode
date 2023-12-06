"""Creating a Linked List from an Input Array"""


class Node:
    """Creating a class Node"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """ A Linked List class to create head and node"""

    def __init__(self):
        self.head = None

    def create_linked_list(self, arr):

        for data in arr:
            # create a new Node
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                current_node = new_node

            else:
                current_node.next = new_node
                current_node = new_node

    def print_linked_list(self):

        current_node = self.head

        while current_node.next is not None:
            print(current_node.data, end='->')
            current_node = current_node.next

        print('None') # to represent that the linked list is over


# Creating a Linked List

arr = [1, 2, 3, 4, 5, 6]
linked_list = LinkedList()
linked_list.create_linked_list(arr)
linked_list.print_linked_list()