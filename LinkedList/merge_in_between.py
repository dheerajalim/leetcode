"""
https://leetcode.com/problems/merge-in-between-linked-lists/description/?envType=daily-question&envId=2024-03-20

The idea is to find the node position in lis1 , after which we need to insert the list2 and the node position in list1
at which we need to connect the end of list2

We iterate over list1 and use start_after variable to point to a node at position a-1,
this way we are at the node whose next should be the head of list2

We now use b-a+2 to calculate the second node in list1 at which list2's end will connect
example a = 2, b = 5
then our end_on node should be node 6 as we need to connect list2 end to 6th node of list1
if we do the math : 5-2+ 2 = 5 i.e is the 6th node (0 based indexing)

After finding start_after, end_on, we connect start_after to head of list2 and then iterate list2 till the
last node and connect the last node of list2 to the end_on node of list1.

Time complexity : O(b + m) , Traversing list2 to find its last node takes O(m) time, where m is the number of nodes
in list2. as a is dominated by b and m is independent of a and b.

Space Complexity : O(1)
"""
from linkedlist import *


def merge_in_between(list1, list2, a, b):
    # initializing the start and end nodes for the connection
    start_after, end_on = list1, list1

    i = 0

    # reaching to a node just before position a
    while i < a - 1:
        start_after = start_after.next
        i += 1

    # since b >= a, hence intializing the end_on with a
    end_on = start_after

    # counting the steps needed to reach after position b
    # this helps to connect end of list2 to this point
    j = b - a + 2

    # updating the end_on node
    while j:
        end_on = end_on.next
        j -= 1

    # get the last node of the list2
    last_node_list2 = list2

    # iterating till the last node of list2
    while last_node_list2.next:
        last_node_list2 = last_node_list2.next

    # making the attachments
    start_after.next = list2
    last_node_list2.next = end_on

    return list1


list1 = [0, 1, 2, 3, 4, 5, 6]
list1 = create_linked_list(list1)
a = 2
b = 2
list2 = [1000000, 1000001, 1000002, 1000003, 1000004]
list2 = create_linked_list(list2)

merged_list = merge_in_between(list1, list2, a, b)

print_linked_list(merged_list)
