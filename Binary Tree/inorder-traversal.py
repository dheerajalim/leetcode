from binary_tree import *

# Inorder : Left Root Right
def inorder_traversal(root):

    if root is None:
        return None

    inorder_traversal(root.left)
    print(root.data, end= " ")
    inorder_traversal(root.right)


root = inserttree()
printtree(root)
print('Inorder Traversal : ')
inorder_traversal(root)