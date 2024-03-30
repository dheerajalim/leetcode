from copy import deepcopy
from typing import Optional
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:

    def make(self, node, visited):
        old_val = node.val
        old_nei = node.neighbors
        new_nei = deepcopy(old_nei)

        new_node = Node(old_val, new_nei)
        visited.append(node)
        for n in old_nei:
            if n not in visited:
                self.make(n, visited)

        return new_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = []
        return self.make(node, visited)


one = Node(1, [])
two = Node(2, [])
three = Node(3, [])
four = Node(4, [])

one.neighbors = [two, three]
two.neighbors = [one, three]
three.neighbors = [two, four]
four.neighbors = [one, three]

obj = Solution()

x = obj.cloneGraph(one)

print(x.val)
for x in x.neighbors:
    print(x.val)