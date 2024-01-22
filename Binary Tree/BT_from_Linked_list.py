from binary_tree import *


def convert(head):
    curr = head
    stack = []
    size = 0
    # this loop will create all the nodes
    # at put that in a stack, so stack[0] is always root
    while curr:
        stack.append(BinaryTree(curr.data))
        size += 1
        curr = curr.next
    # we iterate through all the nodes now
    # to create the left and right links
    for i in range(len(stack)):
        # use the formula
        left = 2 * i + 1
        # if left index is out of bound break
        # else make it as left of current node in stack, stack[i]
        if left > len(stack) - 1:
            break
        stack[i].left = stack[left]
        right = 2 * i + 2
        # if right index is out of bound break
        # else make it as right of current node in stack, stack[i]
        if right > len(stack) - 1:
            break
        stack[i].right = stack[right]

    # return stack[0] which is the root
    return stack[0]
