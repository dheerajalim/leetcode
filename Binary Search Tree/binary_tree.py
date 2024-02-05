class BinaryTree(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inserttree():
    rootdata = int(input())
    root = BinaryTree(rootdata)

    if root.data == -1:
        return None

    leftdata = inserttree()
    rightdata = inserttree()

    root.left = leftdata
    root.right = rightdata

    return root


def printtree(root):
    if root is None:
        return

    print(root.data, end=": ")

    if root.left is not None:
        print("L", root.left.data, end=",")

    if root.right is not None:
        print("R", root.right.data, end=" ")

    print()

    printtree(root.left)
    printtree(root.right)