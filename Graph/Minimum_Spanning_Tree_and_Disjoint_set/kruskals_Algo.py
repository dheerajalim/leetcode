"""
Kruskal Algo gives the weight of MST.

This uses Disjoint set to check if the vertices belong to same component, if yes
then we do not take the weight else we add the weight and applu unionby rank or union by size to these vertices

Steps
1. Whatever the input of graph is given , lets make it in the form on [weight, u, v]
2. Sort the list in ascending order based on the weights
3. Now iterate over the weights and see if they have the same ulimate parent (same compponent), if yes
    then they are forming a cycle, hence we ignore them
4. If the ultimate parent are different for vertex u and v, then we can add their weight to MST and do
    union by rank or size on these vertices
5. Return the MST weight
"""

from disjoint_set_by_rank import *


def kruskal_algo(n, graph):
    # assuming that the input is given as graph = [v, weight]
    # so index 0 will have edge beterr 0 and v with weight w

    # creating a edges in form of [w, u, v]
    edges = []
    for u in range(n):
        for v, w in graph[u]:
            edges.append([w, u, v])

    # sorting on the weights of each edge
    edges = sorted(edges)

    disjoint = Disjoint(n)

    mst_wt = 0
    mst_path = []
    for w, u, v in edges:

        if disjoint.find_uparent(u) != disjoint.find_uparent(v):
            mst_wt += w
            mst_path.append([u,v])
            disjoint.union_by_rank(u, v)
    print(mst_path)
    return mst_wt


n = 3
graph = [[[1, 5], [2, 1]], [[0, 5], [2, 3]], [[1, 3], [0, 1]]]

print(kruskal_algo(n, graph))
