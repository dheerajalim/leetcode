from binary_tree import *

from collections import deque


# the idea is to use level order traversal
# along with a flag to reverse the direction
def zig_zag_traversal(root):
    if root is None:
        return None
    # Boolean Flag
    reverse_order = False
    dq = deque()
    dq.append(root)
    # to store the traversal result
    zig_zag_result = []

    while dq:
        # current size of the deque
        size = len(dq)
        # variable to store the current level nodes
        level_nodes = []
        for i in range(size):
            current_node = dq.popleft()
            # appending the current level nodes to list
            level_nodes.append(current_node.data)
            # adding the left and right nodes to dequeue
            if current_node.left:
                dq.append(current_node.left)
            if current_node.right:
                dq.append(current_node.right)
        # if the boolean flag is true, reverse level_nodes array
        # and append it to result list else just append as is
        if reverse_order:
            zig_zag_result.append(level_nodes[::-1])
        else:
            zig_zag_result.append(level_nodes)
        # update the flag with each level iteration
        reverse_order = not reverse_order

    return zig_zag_result


root = inserttree()
print(zig_zag_traversal(root))
