# use level order traversal

from binary_tree import *

from collections import deque


def max_width(root):
    if root is None:
        return None

    dq = deque()
    # add the root and the index at level
    dq.append([root, 0])
    # to store the level width, by default 1, as we atelast have root node
    max_width = 1

    while dq:
        # to store the first and last node on a level
        # for formula last - first + 1
        first, last = None, None
        # for each level, the queue front will be the min index for that level
        # we store it handy
        min_i = dq[0][1]

        size = len(dq)
        # iterate for each level, to know the level width
        for i in range(size):

            current_node, current_i = dq.popleft()
            # update the index by subtracting the min of that level index from
            # each index, this helps to avoid integer overflow
            # technically the first index value in each level is the min
            # which we store in min_i at each iteration
            current_i = current_i - min_i

            # append the left nodes to queue and add the index
            # using 2i + 1 formula
            if current_node.left:
                dq.append([current_node.left, (2 * current_i) + 1])
            # append the right nodes to queue and add the index
            # using 2i - 1 formula
            if current_node.right:
                dq.append([current_node.right, (2 * current_i) + 2])
            # to keep track of the first node of level
            if i == 0:
                first = current_i
            # to keep track of the last node of level
            if i == size - 1:
                last = current_i
        # the width is last - first node of a level + 1
        # we store the max of the prev and current value
        max_width = max(max_width, last - first + 1)

    # return the max width
    return max_width
