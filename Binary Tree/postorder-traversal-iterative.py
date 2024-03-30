from binary_tree import *


def postorder_traversal(root):
    if root is None:
        return
    # maintain two stacks
    stack1, stack2 = [], []
    # add the root to stack 1
    stack1.append(root)

    while stack1:
        # the top of stack1 is the current node
        curr = stack1.pop()
        # append the curr node data to stack 2
        stack2.append(curr.data)
        # also update stack 1 with node's left and nodes' right
        if curr.left:
            stack1.append(curr.left)
        if curr.right:
            stack1.append(curr.right)
    # the reverse of stack2 is the postorder
    print(stack2[::-1])


root = inserttree()
postorder_traversal(root)
