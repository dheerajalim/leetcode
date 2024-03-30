# this can be solved by getting a preorder
# then keeping two pointer, one on index 0 - arr[i]
# other on index n - arr[j] , then if the arr[i] + arr[j] > sum,
# then j - 1 else of sum > arr[i] + arr[j], then i + 1

# using the iterator concept to reduce the space and time complexity

from binary_tree import *


class BSTIterator:

    def __init__(self, root, reverse=False):
        self.stack = []
        # if reverse is true , then we follow
        # the reveser inorder traversal
        # Right Root Left
        self.reverse = reverse
        curr = root
        self.push_node(curr)

    def push_node(self, curr):
        while curr:
            self.stack.append(curr)
            if self.reverse:
                curr = curr.right
            else:
                curr = curr.left

    def next(self) -> int:
        item = self.stack.pop()

        if self.reverse:
            self.push_node(item.left)
        else:
            self.push_node(item.right)

        return item.data

    def hasNext(self) -> bool:

        return len(self.stack) != 0


def findTarget(root, k):
    if root is None:
        return False

    next_iterator = BSTIterator(root)
    before_iterator = BSTIterator(root, reverse=True)
    # keeping the pointer 1 on the arr[0]
    # keeping pointer 2 at arr[n]
    left_pointer = next_iterator.next()
    right_pointer = before_iterator.next()
    # then follow the two sum algo
    # check the left most and rightmost
    # element and their sum
    while left_pointer < right_pointer:
        # if sum is greater than k, reduce p2 before
        if left_pointer + right_pointer > k:
            right_pointer = before_iterator.next()
        # if sum is smaller than k, move p1 next
        elif left_pointer + right_pointer < k:
            left_pointer = next_iterator.next()
        else:
            return True

    return False


root = inserttree()
# printtree(root)

obj = BSTIterator(root)
