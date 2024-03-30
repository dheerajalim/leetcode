from binary_tree import *


def preorder_traversal(root):
    if root is None:
        return None

    stack = []
    curr = root

    while curr:
        print(curr.data, end=" ")
        stack.append(curr)
        curr = curr.left

    while stack:

        curr = stack.pop()

        curr = curr.right

        while curr:
            print(curr.data, end=" ")
            stack.append(curr)
            curr = curr.left


def preorder_traversal_2(root):
    if root is None:
        return

    # Preorder : Root Left Right
    # hence push the root to stack
    stack = [root]

    while stack:
        # print the top of the stack
        curr = stack.pop()
        print(curr.data, end=" ")
        # since stack is LIFO, hence we push the right first
        # then left, as when we pop, we get left first,
        # so the order Root LEft right is maintained
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)


root = inserttree()
preorder_traversal_2(root)
