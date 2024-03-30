def diagonalSum(mat) -> int:
    # get the number of row or columns, then for the secondary diagonal
    # subtract the num of cols from the primary diagonal col value
    # 0,0. 0,3
    # 1,1. 1,2
    # 2,2. 2,1
    # 3,3. 3,0

    num_cols = len(mat)
    diagonal_sum = 0
    # primary diagonal value
    for point in range(num_cols):
        primary = (point,point)
        secondary = (point, (num_cols-1) - point)

        a = mat[point][point]
        b = mat[point][(num_cols - 1) - point]
        if primary == secondary:
            diagonal_sum += a
        else:
            diagonal_sum += a+b


    return diagonal_sum

mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]

print(diagonalSum(mat))