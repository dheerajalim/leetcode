"""
https://leetcode.com/problems/all-elements-in-two-binary-search-trees/description/
"""
from binary_tree import *
class Solution:
    def inorder_traversal(self, root, arr):

        if root is None:
            return None
        self.inorder_traversal(root.left, arr)

        arr.append(root.data)

        self.inorder_traversal(root.right, arr)

    def sort_arr(self, arr1, arr2):
        result = []
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):

            if arr1[i] > arr2[j]:
                result.append(arr2[j])
                j += 1

            elif arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr1[i])
                result.append(arr2[j])
                i += 1
                j += 1

        while i < len(arr1):
            result.append(arr1[i])
            i += 1

        while j < len(arr2):
            result.append(arr2[j])
            j += 1

        return result

    def getAllElements(self, root1, root2):

        arr1, arr2 = [], []
        self.inorder_traversal(root1, arr1)

        self.inorder_traversal(root2, arr2)

        if arr1 and arr2:
            result = self.sort_arr(arr1, arr2)
            return result

        elif arr1 and not arr2:
            return arr1
        else:
            return arr2


root1 = inserttree()

root2 = inserttree()
obj = Solution()
res = obj.getAllElements(root1, root2)
print(res)