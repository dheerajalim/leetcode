from binary_tree import *


# a balanced binary tree is a tree
# with abs diff between leh and rh is not greater than 1
def is_balanced(root):
    # base condition
    if root is None:
        return 0
    # checking the left height
    lh = is_balanced(root.left)
    # in case if the left subtree return -1, then we will just
    # know it is not balanced , hence return -1
    if lh == -1:
        return -1
    # in case if the right subtree return -1, then we will just
    # know it is not balanced , hence return -1
    rh = is_balanced(root.right)
    if rh == -1:
        return -1
    # checking the abs height diff for lh and rh
    # for balanced tree it should be <= 1
    if abs(lh - rh) > 1:
        return -1

    # return the lh or rh depending on the caller function
    return max(lh, rh) + 1


def check_balanced(root):
    if is_balanced(root) != -1:
        return True

    return False


root = inserttree()
print(check_balanced(root))
