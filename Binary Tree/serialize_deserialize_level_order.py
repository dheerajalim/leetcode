from binary_tree import *

from collections import deque


# Use Level Order Traversal
class Solution:

    def serialize(self, root):
        # this string will store nodes in , seperated form
        # the NULL is replaced by #
        serialized_string = ""
        # if the root is None, we return "#"
        # to denote None
        if root is None:
            return "#"
        # create a queue and just do level order traversal
        dq = deque()
        dq.append(root)
        # add the root to the queue
        serialized_string += str(root.data) + ","
        while dq:
            current = dq.popleft()

            if current.left:
                dq.append(current.left)
                # with each node of the level update the string as well
                serialized_string += str(current.left.data) + ","
            else:
                serialized_string += "#,"

            if current.right:
                dq.append(current.right)
                serialized_string += str(current.right.data) + ","
            else:
                serialized_string += "#,"
        # return the serialized string, with removing the last ,
        return serialized_string[0:-1]

    # here we again use level order traversal idea
    def deserialize(self, data):
        # condition to check for empty tree
        if len(data) == 0:
            return None
        # if the first item is #, this is an empty tree
        if data and data[0] == "#":
            return None
        # if the tree is not None, then we
        # convert string to array by splitting on ,
        if data and len(data) > 1:
            data = data.split(',')

        # again use level order traversal concept
        # add the first item from serialized string array
        # to queue and then iterate until queue is empty
        # for each iteration we see two items in the array
        # which will be left and right nodes, hence
        # at the end pos is increment by 2
        dq = deque()
        root = BinaryTree(data[0])
        dq.append(root)
        pos = 0
        while dq:
            # pop the front of queue, this is the current node
            # create it's left and right child
            current = dq.popleft()
            # increment the array pos, by 1, this is the left child of
            # current Node, if it is "#"  we skip
            pos += 1
            if data[pos] != "#":
                current.left = BinaryTree(data[pos])
                dq.append(current.left)
            # increment the array pos again, by 1, this is the right child of
            pos += 1
            if data[pos] != "#":
                current.right = BinaryTree(data[pos])
                dq.append(current.right)

        return root


obj = Solution()
root = inserttree()
data = obj.serialize(root)
print(data)
root = obj.deserialize(data)

printtree(root)
