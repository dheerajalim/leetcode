"""
Union Find usage

1. Create a parent of each nodes as itself
2. if the parent of both the nodes is same then this edge makes cycle

cannot use DFS here, because we can find cycle but since we need to return the last node
that forms cycle hence we would need union find.



I tried DFS but test case fail for finding last edge that makes cycle
"""


# this is the finf operation of union-find
def find_parent(n, parent):
    # if the current node becomes it's own parent
    # then we return else recursively call until node
    # and its parent are same
    if parent[n] == n:
        return n

    return find_parent(parent[n], parent)


def redundant_connection(edges):
    # since nodes start from 1, we take +1
    n = len(edges) + 1

    # create a parent list where each node will be
    # its own parent initially

    # to store the result
    res = None

    parent = [i for i in range(n)]

    # now we take each edge and check for its parent
    # if both the parent are same, then that edge nakes
    # a cycle , else we update the parent

    for u, v in edges:
        p1 = find_parent(u, parent)
        p2 = find_parent(v, parent)

        # if both the parents are same, then a cycle is formed
        if p1 == p2:
            # since we need to get the last edge that is redundant,
            # we store in res, else we would have just returned
            res = [u, v]
        # if not then we update the parent of p1 to p2
        # this is actually the final parent update
        # that why it is not parent[u] = v
        else:
            # this is union operation of union-find
            parent[p1] = p2

    return res


edges = [[1, 2], [1, 3], [2, 3]]
edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
edges = [[1,5],[3,4],[3,5],[4,5],[2,4]]
edges = [[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]
edges = [[1,5],[3,4],[3,5],[4,5],[2,4]]
edges = [[20,24],[3,17],[17,20],[8,15],[14,17],[6,17],[15,23],[6,8],[15,19],[16,22],[7,9],[8,22],[2,4],[4,11],[22,25],[6,24],[13,19],[15,18],[1,9],[4,9],[4,19],[5,10],[4,21],[4,12],[5,6]]
print(redundant_connection(edges))
