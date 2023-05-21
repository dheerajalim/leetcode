class Node(object):

    def __init__(self, data):
        self.value = data
        self.next = None


# linked list did not work as the nodes cannot be connected properly from the input paths
# Example : paths = [["A","B"],["C","D"],["B","E"],["E","C"],["D","F"]]

# def traverse(paths):
#     head , tail = None, None
#     for path_from, path_to in paths:
#
#         from_node = Node(path_from)
#         to_node = Node(path_to)
#
#         if head is None and tail is None:
#             from_node.next = to_node
#             head = from_node
#             tail = to_node
#
#         else:
#             if from_node.value == tail.value:
#                 tail.next = to_node
#                 tail = to_node
#
#             elif to_node.value == head.value:
#                 from_node.next = head
#                 head = from_node
#
#         print(head.value,tail.value)
#
#
#     return tail.value


def traverse(paths):

    # create a dictionarty with key value pair from the list
    route_dict = dict()

    for from_point, to_point in paths:

        route_dict[from_point] = to_point

    for k, v in route_dict.items():

        if route_dict.get(v):
            continue
        else:
            return v





paths = [["A","B"],["C","D"],["B","E"],["E","C"],["D","F"]]
paths = [["qMTSlfgZlC","ePvzZaqLXj"],["xKhZXfuBeC","TtnllZpKKg"],["ePvzZaqLXj","sxrvXFcqgG"],["sxrvXFcqgG","xKhZXfuBeC"],["TtnllZpKKg","OAxMijOZgW"]]

print(traverse(paths))








   # A > B > E > C > D > F

