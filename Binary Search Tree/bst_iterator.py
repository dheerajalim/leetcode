from binary_tree import *


class BSTIterator:

    def __init__(self, root):
        # stack to store the nodes
        self.stack = []
        curr = root
        # follow the inorder traversal
        # keep on moving to the left
        # and store the elements to the stack
        while curr:
            self.stack.append(curr)
            curr = curr.left

    def next(self) -> int:
        # the top of stack is the next element
        item = self.stack.pop()
        # once the item is poped, we need to fetch the right nodes
        # add all the nodes on the left of the right node of the current node
        curr = item.right
        while curr:
            self.stack.append(curr)
            curr = curr.left

        return item.data

    def hasNext(self) -> bool:
        # to check of the next element is present
        # if the stack is empty then hasNext will be false
        return len(self.stack) != 0


root = inserttree()
# printtree(root)

obj = BSTIterator(root)
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.hasNext())
print(obj.hasNext())
