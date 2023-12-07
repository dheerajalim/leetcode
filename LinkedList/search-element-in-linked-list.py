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


def search_element(head, element):

    # Given the element and head of the Linked list
    # returning -1 means, element not found
    # Otherwise return the index of the element

    if head is None:
        return -1

    current_position = head

    index = 0

    while current_position is not None:
        # looping in the LL until we reach the end of the LL
        if current_position.data == element: # if the node data matches the element to search then return the index
            return index

        # keep on updating the current position in case no match is found
        current_position = current_position.next
        index += 1

    return -1  # reaches here means , input element was not present


arr = []
head = create_linked_list(arr)

print(search_element(head, 52))
