"""

By size means that the array will maintain a rank
size is update based on how many nodes are connected.
Size of a node means the number of nodes connected to it

TC : O(4 alpha) i.e Contant time
"""


class Disjoint:

    def __init__(self, n: int):
        # the number of vertices
        self.n = n
        # the initial size will be 1 for all
        self.size = [1] * n
        self.parent = [i for i in range(n)]

    def find_uparent(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.find_uparent(self.parent[node])
        return self.parent[node]

    def union_by_size(self, u, v):

        # if the ultimate parent is same then they are already connected
        up_u = self.find_uparent(u)
        up_v = self.find_uparent(v)

        if up_u == up_v:
            return

        else:
            # if size of ultimate parent of u is less than ultimate parent of v,
            # then update the up_u as up_v, and update the size by adding size of up_u and up_v
            if self.size[up_u] < self.size[up_v]:
                self.parent[up_u] = up_v
                self.size[up_v] += self.size[up_u]

            # similar case as above just the up_u higher size than up_v
            elif self.size[up_v] < self.size[up_u]:
                self.parent[up_v] = up_u
                self.size[up_u] += self.size[up_v]

            # if both have the same size, then any one can be taken
            elif self.size[up_v] == self.size[up_u]:
                # in this case we can attach anyone to anyone
                self.parent[up_v] = up_u
                self.size[up_u] += self.size[up_v]


n = 7
disjoint_obj = Disjoint(n)
disjoint_obj.union_by_size(0, 1)
disjoint_obj.union_by_size(1, 2)
disjoint_obj.union_by_size(3, 4)
disjoint_obj.union_by_size(5, 6)
disjoint_obj.union_by_size(4, 5)

if disjoint_obj.find_uparent(2) == disjoint_obj.find_uparent(6):
    print('Same Parent')
else:
    print('No')

disjoint_obj.union_by_size(2, 6)
if disjoint_obj.find_uparent(2) == disjoint_obj.find_uparent(6):
    print('Same Parent')
else:
    print('No')

print(disjoint_obj.parent)
print(disjoint_obj.size)
