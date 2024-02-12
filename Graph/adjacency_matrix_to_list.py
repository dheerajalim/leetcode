"""
convert adjacency matrix to list
"""


def matrix_to_list(matrix):
    adj_list = [[] for _ in range(len(matrix))]
    for i in range(len(matrix)):

        for j in range(len(matrix[i])):
            # self nodes are not considered i.e i != j
            # and if there is a 1 , then this is a edge
            if i != j and matrix[i][j] == 1:
                adj_list[i].append(j)

    return adj_list


matrix = [[1, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 1]]

print(matrix_to_list(matrix))
