def max_area_histogram(arr, size):
    nse_left, nse_right = [], []
    nse_left_index, nse_right_index = [], [size] * size

    i, j = 0, size - 1

    while i < size:

        while nse_left and arr[i] <= nse_left[-1][0]:
            nse_left.pop()

        if nse_left:
            nse_left_index.append(nse_left[-1][1])
            nse_left.append((arr[i], i))

        else:
            nse_left.append((arr[i], i))
            nse_left_index.append(-1)

        i += 1

    while j >= 0:

        while nse_right and arr[j] <= nse_right[-1][0]:
            nse_right.pop()

        if nse_right:
            nse_right_index[j] = nse_right[-1][1]
            nse_right.append((arr[j], j))

        else:
            nse_right.append((arr[j], j))
            nse_right_index[j] = size

        j -= 1

    result = []

    for i in range(size):
        result.append(((nse_right_index[i] - nse_left_index[i]) - 1) * arr[i])

    return max(result)


def max_area_binary_matrix(matrix):
    # The idea here is to consider the 2d Binary matrix as 1 D
    # We will assume each row as the height of the histogram
    # that way each row acts as a building, similarly to 1d question

    # getting the dimensions of the matrix
    height, width = len(matrix), len(matrix[0])
    # variable to store the max area
    max_area = 0
    # an array to store the prev histogram details for
    # initializing the histogram array
    histogram = [0] * width
    # lopping through each row
    for i in range(height):

        for j in range(width):
            # if the current element is not a 0, means a histogram exists
            # add the previous row histogram height to it
            if matrix[i][j] != 0:
                histogram[j] = matrix[i][j] + histogram[j]
            # if not , then just assume 0 height histogram
            else:
                histogram[j] = 0
        # for each row of 2d array, we pass that as a histogram
        # find the max area of histogram and then return max value
        max_area = max(max_area, max_area_histogram(histogram, width))

    return max_area


matrix = [[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]]

matrix = [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]
print(max_area_binary_matrix(matrix))
