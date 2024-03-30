from binary_tree import *


def find_max_path(root, maxi):
    if root is None:
        return 0
    # at any point returning a -ve number will reduce the
    # path sum, hence we use max(0 , return value)...
    # where if a -ve number is returned we make it 0
    # in order to avoid those paths with -ve path sum
    left_max = max(0, find_max_path(root.left, maxi))
    right_max = max(0, find_max_path(root.right, maxi))
    # while calculating the maximum path, we take the left max
    # right max and root node and sum them and return the max of
    # new value and existing maxi
    maxi[0] = max(maxi[0], left_max + right_max + root.data)

    # while returning to the parent root, we return the
    # max value of left side or right side + node value
    # as this will form the path
    return max(left_max, right_max) + root.data


def max_path_sum(root):
    maxi = [float('-inf')]

    find_max_path(root, maxi)

    return maxi[0]


root = inserttree()

print(max_path_sum(root))
