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


def length_linked_list(head): # Input is the LL head

    # Checking for the base conditions to avoid unnecessary steps
    if head is None :
        return 0
    elif head.next is None:
        return 1

    # Strating the while loop to get the length of the LL
    length = 0
    current_position = head

    # We loop until the current position is Not None
    while current_position is not None:
        # Keep on updating the length counter with each new Node and update the position to next position as well
        length += 1
        current_position = current_position.next

    # return the calculated length
    return length


arr = [44,44]
head = create_linked_list(arr)

print(length_linked_list(head))