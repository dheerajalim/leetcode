class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list(arr):
    head = None
    current_position = None
    for data in arr:

        if head is None:
            head = Node(data)
            current_position = head

        else:
            current_position.next = Node(data)
            current_position = current_position.next

    return head


def print_linked_list(head):

    current_position = head

    while current_position is not None:
        print(current_position.data, end='->')
        current_position = current_position.next
    print('None')
