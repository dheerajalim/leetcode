from binary_tree import *


# Postorder :  Left Right Root
def postorder_traversal(root):
    if root is None:
        return None

    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end=" ")


root = inserttree()
printtree(root)
print('Postorder traversal : ')
postorder_traversal(root)
