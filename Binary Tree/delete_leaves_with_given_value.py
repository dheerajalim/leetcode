"""
https://leetcode.com/problems/delete-leaves-with-a-given-value/description/?envType=daily-question&envId=2024-05-17
"""

def remove_leaf_nodes(root, target):

    if root is None:
        return

    if root.left is None and root.right is None:
        