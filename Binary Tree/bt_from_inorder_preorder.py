from binary_tree import *


# the first node of preorder is the root
# when you find this element in inorder,
# the left part is left subtree
# the right part is right subtree

class Solution:

    def __init__(self):
        self.hashmap = dict()
        self.preorder_index = 0

    def create_indexing(self, inorder: list):
        for i, j in enumerate(inorder):
            self.hashmap[j] = i

    def create_binary_tree(self, preorder, inorder, si_in, ei_in):

        # edge case for condition like  for pre = [10,20] and in [20,10]
        # here the si > ei
        if si_in > ei_in:
            return None

        root = BinaryTree(preorder[self.preorder_index])
        self.preorder_index += 1

        # condition for leaf nodes
        if si_in == ei_in:
            return root

        # finding the root in inorder list
        i = self.hashmap[root.data]

        root.left = self.create_binary_tree(preorder, inorder, si_in, i - 1)
        root.right = self.create_binary_tree(preorder, inorder, i + 1, ei_in)

        return root


preorder = [10, 20, 30, 40, 50]
inorder = [20, 10, 40, 30, 50]
sol = Solution()
sol.create_indexing(inorder)

root = sol.create_binary_tree(preorder, inorder, 0, len(inorder) - 1)

printtree(root)
