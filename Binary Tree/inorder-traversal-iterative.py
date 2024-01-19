from binary_tree import *


def inorder_traversal(root):
    if root is None:
        return

    stack = []
    curr = root
    # move to the extreme left node
    while curr:
        stack.append(curr)
        curr = curr.left
    # the top of stack contains the leftmost node
    while stack:
        # pop the top of the stack
        curr = stack.pop()
        print(curr.data, end=" ")
        # check if the right node exists,
        # if yes, then push it to stack and
        # iteratively get all it left nodes as well
        curr = curr.right
        while curr:
            stack.append(curr)
            curr = curr.left


root = inserttree()
inorder_traversal(root)
