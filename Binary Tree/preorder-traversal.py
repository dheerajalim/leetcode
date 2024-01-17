from binary_tree import *


# Preorder : Root Left Right
def preorder_traversal(root):
    if root is None:
        return None

    print(root.data, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)


root = inserttree()
printtree(root)
print('Preorder traversal : ')
preorder_traversal(root)
