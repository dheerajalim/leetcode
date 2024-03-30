from binary_tree import *


def inorder_successor(root, val):
    successor = None

    # successor to store the value of successor
    def find_successor(root, val, successor):
        # if root is None, we return the successor
        # as that is the value we are looking for
        if root is None:
            return successor

        # if the node value <= given value
        # that means node is anyways smaller or equal than given val
        # hence it cannot be the successor,
        # hence me move to right to find bigger value
        if root.data <= val:
            return find_successor(root.right, val, successor)

        # here the root is greater than val, hence this is a possible
        # successor, hence we can have other possible more closer
        # candidate for successor, hence we move left towards smaller values
        # but greater than val
        if root.data > val:
            successor = root.data

            return find_successor(root.left, val, successor)

    # the function when find none return successor
    # hence this call will return successor
    return find_successor(root, val, successor)


def inorder_successor_iterative(root, val):
    if root is None:
        return None
    successor = None
    curr = root
    # keep on moving until curr is not None
    while curr:
        # if the node is smaller/equal, move right for greate value
        # if node is greater, possible candidate for successor
        # hence move left for closer values to val
        if val >= curr.data:
            curr = curr.right

        elif val < curr.data:
            successor = curr.data
            curr = curr.left

    return successor


root = inserttree()
val = 8
print(inorder_successor(root, val))
print(inorder_successor_iterative(root, val))
