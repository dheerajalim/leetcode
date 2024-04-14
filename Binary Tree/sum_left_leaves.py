"""
https://leetcode.com/problems/sum-of-left-leaves/description/?envType=daily-question&envId=2024-04-14

1. Level Order Travesal.
2. Update the queue with left node and position 0
3. Update the queue with right node and position 1
2. Add to sum if the node is leaf node and its position is 0
"""

from binary_tree import *
from collections import deque


def sum_left_leaves(root):
    dq = deque()

    dq.append([root, 1])
    sum_left = 0
    while dq:

        node, position = dq.popleft()
        if node and node.left:
            # store the left node in queue along with position
            dq.append([node.left, 0])

        if node and node.right:
            # store the right node in queue along with position
            dq.append([node.right, 1])

        # if the node is a left leaf node, we add it to the sum of left leaf nodes
        if node and node.left is None and node.right is None and position == 0:
            sum_left += node.data

    return sum_left


root = inserttree()
# printtree(root)
print(sum_left_leaves(root))
