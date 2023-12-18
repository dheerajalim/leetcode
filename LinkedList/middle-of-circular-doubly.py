# Given a circular doubly linked list of odd size n, the task is to print the middle element.

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def create_circular_doubly_linked_list(arr):
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

    # Makes it circular
    curr.next = head
    head.prev = curr
    return head


def print_linked_list(head):

    current_position = head

    while current_position is not None:
        print(current_position.data, end='->')
        current_position = current_position.next
        if current_position == head:
            print(f'...')
            return


def findMiddle(head):
    # Fetching the last node of the LL
    tail_node = head.prev

    # In case a single node is present, that is the middle
    if head.next is None:
        return head.data

    slow_ptr = head
    fast_ptr = head
    # Iterat till the fast_ptr reaches the last node
    while fast_ptr != tail_node:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next

    return slow_ptr.data


print('Creating a doubly Linked List')
arr = [1, 2, 3, 4, 5, 6, 7]
head = create_circular_doubly_linked_list(arr)
print_linked_list(head)
print(findMiddle(head))