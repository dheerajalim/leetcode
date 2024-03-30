# We are assuming that the elements in the linked list are unique
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


# case where the head needs to be removed
def remove_head(head):

    new_head = head.next

    return new_head




def delete_node_value(head, node):


    if head is None:
        return head

    if head.data == node:
        head = remove_head(head)
        return head

    current_position = head

    while current_position.next is not None:

        if current_position.data == node:
            # updating the current node with the next node value
            current_position.data = current_position.next.data

            # Making the new connection from current node to the next of next node, which basically skips the next node
            current_position.next = current_position.next.next

            return head

        # case where we have reached the last node and this node matches the node to be deleted
        if current_position.next.next is None and current_position.next.data == node:
            current_position.next = None
            return head

        current_position = current_position.next

    return head


def delete_node_position(head, position):

    if head is None:
        return None

    # this means that the head needs to be updated
    if position == 0 : # the head needs to be removed
        head = remove_head(head)
        return head

    current_position = 0 # starting at the 0th position
    temp_head = head # defining the temp head

    while temp_head.next is not None:
        # if the position matches the input position
        if current_position == position:
            temp_head.data = temp_head.next.data
            temp_head.next = temp_head.next.next
            return head

        # case when the position is the tail of the linked list
        if temp_head.next.next is None and current_position + 1 == position:
            temp_head.next = None
            return head

        # update the position count and the temp_head to next node
        current_position += 1
        temp_head = temp_head.next

    return head


arr = [1, 2, 3, 4]

print('==== Delete by Node =====')
head = create_linked_list(arr)
print_linked_list(head)

head = delete_node_value(head, 2)
print_linked_list(head)

print('===== Delete By Position =====')
head = create_linked_list(arr)
print_linked_list(head)

head = delete_node_position(head, 2)
print_linked_list(head)