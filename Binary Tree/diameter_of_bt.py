from binary_tree import *


# follows the concept of finding the height
# of BT, we jsus insert one variation
# i.e max (result, 1 + lh + rh) > this is the diameter
def calculate_diameter(root, result: list):
    if root is None:
        return 0

    lh = calculate_diameter(root.left, result)
    rh = calculate_diameter(root.right, result)

    result[0] = max(result[0], 1 + lh + rh)

    return max(lh, rh) + 1


def diameter(root):
    # default value to -inf, to allow it to be updated
    # using a list, to help us update with reference
    result = [float('-inf')]

    calculate_diameter(root, result)

    return result[0]

root = inserttree()
print(diameter(root))
