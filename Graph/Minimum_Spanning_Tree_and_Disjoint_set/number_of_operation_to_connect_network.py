from disjoint_set_by_rank import *


def make_connected(n, connections):
    # to get the count of connections that can be broken
    # from the network
    break_connection = 0
    disjoint = Disjoint(n)

    # find the disjoint set
    for u, v in connections:

        up_u = disjoint.find_uparent(u)
        up_v = disjoint.find_uparent(v)

        # if the ultimate parent is same, then this connection
        # can be broken, hence increase the count
        if up_u == up_v:
            break_connection += 1
        # else union the nodes
        else:
            disjoint.union_by_rank(u, v)

    # calculate connected components
    # if the index and its parent are same that means it is the ultimate parent
    # so no of ultimate parents are actual the count of connected components
    count = 0
    for i in range(len(disjoint.parent)):
        if i == disjoint.parent[i]:
            count += 1
    """Another possible way to get the connected components is to use the disjoint class component
    count = disjoint.component
    """

    # if the total possible connection that can be broken are ore than
    # or equal to the required edges for connecting the components
    # then return the count-1 else -1
    if break_connection >= count - 1:
        return count - 1

    return -1


n = 6
connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]

print(make_connected(n, connections))
