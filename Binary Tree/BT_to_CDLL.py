# convert Binary Tree to Circular Doubly Linked List

from binary_tree import *


class Solution():

    def __init__(self):
        self.prev = None
        self.head = None

    # uses the same logic od DLL , just add the
    # relation between the last node and the head
    def bt_to_cdll(self, root):

        if root is None:
            return None

        self.bt_to_cdll(root.left)

        if self.prev is None:
            self.head = root

        else:
            self.prev.right = root
            root.left = self.prev

        self.prev = root

        self.bt_to_cdll(root.right)

        # the prev at the recursion completion points to the
        # last node in the DLL, we create connection between
        # prev and head to make CDLL
        self.prev.right = self.head
        self.head.left = self.prev

    def print_linked_list(self, head):

        curr = head
        i = 1
        while curr and i <= 9:
            print(curr.data, end=" ")
            if curr.right is None:
                last = curr
            curr = curr.right
            i += 1
        # while last:
        #     print(last.data, end= " ")
        #     last = last.left


obj = Solution()
root = inserttree()

obj.bt_to_cdll(root)

obj.print_linked_list(obj.head)
