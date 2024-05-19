"""
https://leetcode.com/problems/evaluate-boolean-binary-tree/description/?envType=daily-question&envId=2024-05-16

0 = False
1 = True
2 - OR
3 = AND
"""

from binary_tree import *


def evaluate_tree(root):
    if root.left is None and root.right is None:
        if root.data == 0:
            return False
        elif root.data == 1:
            return True

    left = evaluate_tree(root.left)
    right = evaluate_tree(root.right)

    if root.data == 2:
        return left or right

    elif root.data == 3:
        return left and right


root = inserttree()

printtree(root)

print("+++++")

print(evaluate_tree(root))
