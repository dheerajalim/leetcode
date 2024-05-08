"""
https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/?envType=daily-question&envId=2024-05-07
"""

from linkedlist import *


def double_it(head):
    # parse the linked list and get the node values to make the number
    # also store the size of the linked list

    number = ""
    count = 0

    curr = head

    while curr:
        count += 1
        number += str(curr.data)
        curr = curr.next

    # double the number
    double_num = str(int(number) * 2)

    if len(double_num) == count:
        curr = head
        for num in double_num:
            curr.data = num
            curr = curr.next

    elif len(double_num) > count:
        extra_len = len(double_num) - count
        new_head = Node(double_num[0])
        curr = new_head
        for num in range(1, extra_len):
            new_node = Node(double_num[num])
            curr = new_node

        curr.next = head
        curr = head
        for num in double_num[extra_len:]:
            curr.data = num
            curr = curr.next

        head = new_head

    return head


arr = [1, 8, 9]
arr = [9, 9, 9]
head = create_linked_list(arr)
print_linked_list(head)

new_head = double_it(head)
print_linked_list(new_head)
