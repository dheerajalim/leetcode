from binary_tree import *


# the last node in postorder is the root
# when we go back by one index from last, that is the right node
# hence we call right and then left side in recursion
class Solution:

    def __init__(self):
        self.hashmap = dict()
        self.postorder_index = 0

    def create_indexing(self, inorder: list):
        for i, j in enumerate(inorder):
            self.hashmap[j] = i

    def create_binary_tree(self, postorder, inorder, si_in, ei_in):
        # edge case for condition like  for pre = [10,20] and in [20,10]
        # here the si > ei
        if si_in > ei_in:
            return None

        # creating the root
        root = BinaryTree(postorder[self.postorder_index])

        # moving to the next root index in postorder list
        self.postorder_index -= 1

        # condition for leaf nodes
        if si_in == ei_in:
            return root

        # finding the root in inorder list
        i = self.hashmap[root.data]

        # since post order is Left Right Root
        # hence when we have the root, the next would be right
        # hence we call right and then left subtree
        root.right = self.create_binary_tree(postorder, inorder, i + 1, ei_in)
        root.left = self.create_binary_tree(postorder, inorder, si_in, i - 1)

        return root


postorder = [40, 50, 20, 60, 30, 10]
inorder = [40, 20, 50, 10, 60, 30]

sol = Solution()
sol.create_indexing(inorder)
sol.postorder_index = len(inorder) - 1
root = sol.create_binary_tree(postorder, inorder, 0, len(inorder) - 1)

printtree(root)
