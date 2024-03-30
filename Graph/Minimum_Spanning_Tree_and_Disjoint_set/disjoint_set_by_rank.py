"""

By Rank means that the array will maintain a rank
Rank here is that a node with higher rank is above node with lower rank

TC : O(4 alpha) i.e Contant time
"""
class Disjoint:

    def __init__(self, n: int):
        # the number of vertices
        self.n = n
        self.rank = [0] * n
        self.parent = [i for i in range(n)]
        self.component = n

    def find_uparent(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.find_uparent(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u, v):

        # if the ultimate parent is same then they are already connected
        up_u = self.find_uparent(u)
        up_v = self.find_uparent(v)

        if up_u == up_v:
            return

        else:
            # if rank of ultimate parent of u is less than ultimate parent of v,
            # then update the up_u as up_v, and no need to increment
            # rank as up_v is already higher rank
            if self.rank[up_u] < self.rank[up_v]:
                self.parent[up_u] = up_v

            # similar case as above just the up_u has higher rank than up_v
            elif self.rank[up_v] < self.rank[up_u]:
                self.parent[up_v] = up_u

            elif self.rank[up_v] == self.rank[up_u]:
                # in this case we can attach anyone to anyone
                self.parent[up_v] = up_u
                self.rank[up_u] += 1

            # whenever a edge is formed, the component count is reduced by 1
            self.component -= 1

# n = 7
# disjoint_obj = Disjoint(n)
# disjoint_obj.union_by_rank(0,1)
# disjoint_obj.union_by_rank(1,2)
# disjoint_obj.union_by_rank(3,4)
# disjoint_obj.union_by_rank(5,6)
# disjoint_obj.union_by_rank(4,5)
#
# if disjoint_obj.find_uparent(2) == disjoint_obj.find_uparent(6):
#     print('Same Parent')
# else:
#     print('No')
#
# disjoint_obj.union_by_rank(2,6)
# if disjoint_obj.find_uparent(2) == disjoint_obj.find_uparent(6):
#     print('Same Parent')
# else:
#     print('No')
#
# print(disjoint_obj.parent)
# print(disjoint_obj.rank)