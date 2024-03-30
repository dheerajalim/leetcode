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


def insert_node(head, new_node, position):

    # case 1 : The new node needs to be inserted at the beginning , which means the head is updated

    if position == 0:

        new_head = Node(new_node)
        new_head.next = head
        return new_head

    # case 2 : Inserting head in between at a position

    current_position = 0
    temp_head = head

    # iterating till the last element of the linked list
    while temp_head is not None:
        # updating the position with each iteration
        current_position += 1
        """
        if the input pos and current pos match that means this is the position at which we need to insert
        Here the temp_head is actually the prev node and its new node should be inserted in between 
        temp_head and it's next node.
        This case also handles insertion at the tail as we are iterating till the last element 'temp_head is not None'
        """
        if current_position == position:
            new_node = Node(new_node)  # creates a new node
            next_node = temp_head.next  # this helps us to know the next node of the new inserted node
            temp_head.next = new_node  # inserts the new node to the required position
            new_node.next = next_node  # updates the next of the new node

            return head

        temp_head = temp_head.next  # keep on moving to next node until a match is found

    return head  # else we return the head from here


arr = [1, 2, 3, 4]
head = create_linked_list(arr)
print_linked_list(head)
print_linked_list(insert_node(head, 52, 3))
