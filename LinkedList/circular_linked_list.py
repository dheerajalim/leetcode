class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_circular_linked_list(arr):
    if len(arr) == 0:
        return None
    head = None
    curr = None
    for data in arr:

        if head is None:
            head = Node(data)
            curr = head
        else:
            curr.next = Node(data)
            curr = curr.next

    curr.next = head
    return head


def print_linked_list(head):

    current_position = head

    while current_position is not None:
        print(current_position.data, end='->')
        current_position = current_position.next
        if current_position == head:
            print(f'...')
            return


# arr = [1, 2, 3, 4, 5]
#
# head = create_circular_linked_list(arr)
#
# print_linked_list(head)
