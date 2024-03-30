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
    if head: curr.next = head
    if head: head.prev = curr
    return head


def print_linked_list(head):
    current_position = head

    while current_position is not None:
        print(current_position.data, end='->')
        current_position = current_position.next
        if current_position == head:
            print(f'...')
            return


def compareCLL(head1, head2):
    # Base condition for empty LL
    if head1 is None and head2 is None:
        return True
    # Condition is the any one is empty LL
    elif head1 is None or head2 is None:
        return False
    # Directly comparing the last node values, if they don't match then return False
    elif head1.prev.data != head2.prev.data:
        return False

    curr1, curr2 = head1, head2
    # iterating till the nodes mismatch or we reach again to head
    while curr1.next != head1 and curr2.next != head2:
        if curr1.data != curr2.data:
            return False

        curr1, curr2 = curr1.next, curr2.next

    # Check the last nodes if there is a mismatch as after the iteration we are at last node
    if curr1.data != curr2.data:
        return False

    return True


print('Compare Circular DLL')
arr = [1, 3, 4, 5, 7]
head1 = create_circular_doubly_linked_list(arr)
print_linked_list(head1)
arr = [1, 3, 4, 5, 6, 7,1,10,11,7   ]
head2 = create_circular_doubly_linked_list(arr)
print_linked_list(head2)
print(compareCLL(head1, head2))
