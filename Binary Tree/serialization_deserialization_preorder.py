# Definition for a binary tree node.
from binary_tree import *


class Solution:

    def __init__(self):
        self.serialize_string = ""
        self.pos = 0

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # if the root is None, return None
        # we represent None by #
        if root is None:
            self.serialize_string += "#,"
            return self.serialize_string

        # this is preorder traversal algo
        self.serialize_string += str(root.data) + ","
        self.serialize(root.left)
        self.serialize(root.right)

        return self.serialize_string

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # convert the string to array and remove the last comma
        data = data.split(',')[:-1]

        def action(data):
            # here we do the pre order traversal
            if data[self.pos] == "#":
                return None

            # the array will keep on moving to left
            # with pos being update to next item in array
            root = BinaryTree(data[self.pos])
            self.pos += 1
            root.left = action(data)
            # the array will keep on moving to right
            # with pos being update to next item in array
            self.pos += 1
            root.right = action(data)
            # return the root
            return root

        root = action(data)

        return root


root = inserttree()
obj = Solution()
data = obj.serialize(root)
print(data)
root = obj.deserialize(data)
printtree(root)
