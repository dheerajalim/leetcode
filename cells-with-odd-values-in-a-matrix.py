
def oddCells(m, n, indices) :
    # creating  m*n matrix with all 0's
    matrix = [[0 for i in range(n)] for j in range(m)]

    count = 0
    for row, col in indices:
        # updating the row
        for i in range(n):
            matrix[row][i] += 1
            if matrix[row][i] % 2 == 1:
                count += 1
            else:
                count -= 1

        for j in range(m):
            matrix[j][col] += 1
            if matrix[j][col] % 2 == 1:
                count += 1
            else:
                count -= 1


    print(matrix, count)






        #[0,1] 0: row, 1: col





# oddCells(2,2,[[1,1],[0,0]])


def test( n: int, m: int, indices) -> int:
    count = 0
    row = [0] * n
    col = [0] * m
    for x, y in indices:
        row[x] += 1
        col[y] += 1
    for i in range(n):
        for j in range(m):
            if (row[i] + col[j]) % 2 == 1:
                count += 1
    return count

test(2,3,[[0,1],[1,1]])

