from binary_tree import *


def floor_bst(root, key, floor):
    # base case to return None
    # if the root is None or floor not found
    if root is None:
        return None

    # if the key is less than we need to move to left
    # also floor is not updated as rood.data is > than it
    if key < root.data:
        floor_bst(root.left, key, floor)

    # if the key is greater than we need to move to right
    # also update the floow as this is > than root.data
    # and a potential floor value
    elif key > root.data:
        floor[0] = root.data
        floor_bst(root.right, key, floor)
    # in case key given is itself present, return that
    else:
        floor[0] = key


def floor_bst_iterative(root, key):
    floor = None

    if root is None:
        return None

    curr = root
    while curr:
        # given key is present itself
        if curr.data == key:
            return curr.data
        # key is smaller the node data
        if curr.data > key:
            curr = curr.left
        # key is greater the node data
        # hence node is a possible floor
        # keep on updating floor with each new value
        # on the right as this is more closer to key
        elif curr.data < key:
            floor = curr.data
            curr = curr.right

    return floor


root = inserttree()

floor = [None]
floor_bst(root, 14, floor)
print(floor_bst_iterative(root, 14))

print(floor[0])
