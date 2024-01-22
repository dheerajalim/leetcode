# https://www.geeksforgeeks.org/batch/ds-with-python/track/tree-advanced-python/problem/construct-binary-tree-from-parent-array

from binary_tree import *

from collections import deque


"""
Uses a hash map , where key is the item from the parent array 
and value is the list of indexes
for example:
{
-1 : [0]
0 : [1,2]
1 : [3 ,4]
3 : [5]
5 : [6]
}

The we parese this hash map, and keep on appending
to the queue, iterating the queue until it is empty.
The item at front of queue will be the parent and we will then
create the left and the right nodes
"""
class Solution1:
    # Function to construct binary tree from parent array.
    def createTree(self, parent, N):
        # your code here
        dq = deque()
        hash_map = {}

        for i in range(N):

            if hash_map.get(parent[i]):
                hash_map[parent[i]].append(i)
            else:
                hash_map[parent[i]] = [i]

        dq.append(BinaryTree(hash_map[-1][0]))
        root = dq[0]
        while dq:
            curr = dq.pop()

            if hash_map.get(curr.data):
                if len(hash_map[curr.data]) == 2:
                    curr.left = BinaryTree(hash_map[curr.data][0])
                    dq.append(curr.left)
                    curr.right = BinaryTree(hash_map[curr.data][1])
                    dq.append(curr.right)
                else:
                    curr.left = BinaryTree(hash_map[curr.data][0])
                    dq.append(curr.left)

        return root


class Solution2:

    def createTree(self, parent, N):
        # this hash m,ap will contain the index : Node(index)
        # this will create all the nodes for us
        hash_map = {}
        for i in range(N):
            hash_map[i] = BinaryTree(i)

        # we traverse through the parent array
        for i in range(N):
            # if the parent array item is -1, we know that it is root
            # we get the node at index i from hash map, and make it root
            if parent[i] == -1:
                root = hash_map[i]
            # else we create other node connections
            else:
                # take the value from parent node index i, this is the parent
                # we check this node in the hash_map
                # we then check that if left node exists, if not we add the
                # current index i node as it left
                if not hash_map[parent[i]].left:
                    hash_map[parent[i]].left = hash_map[i]
                # if left is present then we add current index i as right node
                elif not hash_map[parent[i]].right:
                    hash_map[parent[i]].right = hash_map[i]

        return root