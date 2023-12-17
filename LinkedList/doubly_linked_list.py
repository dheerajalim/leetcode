class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def create_doubly_linked_list(arr):
    head = None

    for data in arr:

        if head is None:
            head = Node(data)
            curr = head

        else:
            new_node = Node(data)
            new_node.prev = curr
            curr.next = new_node
            curr = new_node

    return head


def print_linked_list(head):
    current_position = head

    while current_position is not None:
        print(current_position.data, end='->')
        current_position = current_position.next

    print('None')


# Creating a Linked List

# arr = [1, 2, 3, 4, 5, 6]
# head = create_doubly_linked_list(arr)
# print_linked_list(head)
