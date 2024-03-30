from disjoint_set_by_rank import *


def remove_stones(stones):
    """
    We treat each row as a node and each col as a node
    since row and col can be same example 1,1. So we convert cols as
    next in sequence of row, so cols = max_rows+max_cols + 2
    if there are  3 rows and 3 cols
        0  1   2
    0
    1
    2
    the rows are : 0, 1, 2
    cols are : 3, 4, 5
    i.e max_row(2) + max_cos(2) + 1 = 5
    since are n = count , so it should be 6  hence max_rows+max_cols + 2
    """
    max_row, max_col = 0, 0

    for i, j in stones:
        max_row = max(max_row, i)
        max_col = max(max_col, j)

    # create a disjoint set
    disjoint = Disjoint(max_row + max_col + 2)
    hash_map = dict()
    # for all the coordinates in the stones, row and col are treates as nodes
    for u, v in stones:
        row = u
        col = v + max_row + 1
        # union the nodes
        disjoint.union_by_rank(row, col)
        # add all the nodes in a map, this is required to check the ultimate parent
        hash_map[row] = 1
        hash_map[col] = 1

    print(disjoint.component)
    count = 0
    # if the ultimate parent of node and itself are same
    # then this is the component
    for k, v in hash_map.items():
        if disjoint.find_uparent(k) == k:
            count += 1
    # the stones that are remove is number of stones in a component -1
    # hence if we have 3 components and 7 total stones
    # so stones that are removed are total_Stones - component count
    print(disjoint.parent)
    return len(stones) - count


stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
# stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# stones = [[0,0]]
# stones = [[0,1],[1,0],[1,1]]
stones = [[0, 1], [1, 1]]
print(remove_stones(stones))
