from binary_tree import *


# to convert a BT into DLL without using extra space
# we will create a DLL in Inorder traversal format

class Solution:

    def __init__(self):
        self.head = None
        self.prev = None

    def binary_to_dll(self, root):
        # base case
        if root is None:
            return None
        # recursively call the left sub tree
        self.binary_to_dll(root.left)
        # if the prev is None, that means we reached the head
        # set the head for DLL
        if self.prev is None:
            self.head = root
        # else we create the link between DLL nodes by setting the left and right pointers
        # the current node will mark its left to prev
        # and prev will mark its right to current
        else:
            root.left = self.prev
            self.prev.right = root
        # and keep on updating the prev value
        # this has to be done always to have the updated prev
        self.prev = root

        # recursively call the right sub tree
        self.binary_to_dll(root.right)

        return self.head



root = inserttree()
obj = Solution()
head = obj.binary_to_dll(root)

print(head.data)
print(head.right.data)
print(head.right.right.data)
print(head.right.right.right.data)
print(head.left)
print(head.right.left.data)
print(head.right.right.left.data)
