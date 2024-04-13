"""
https://leetcode.com/problems/maximal-rectangle/description/?envType=daily-question&envId=2024-04-13
"""


def histogram_area(heights):
    n = len(heights)
    nse_left, nse_left_index = [], []
    nse_right, nse_right_index = [], [-1] * n

    # calculating the nse left
    i = 0

    while i < n:

        while nse_left and heights[i] <= nse_left[-1][0]:
            nse_left.pop()

        if nse_left:
            nse_left_index.append(nse_left[-1][1])
            nse_left.append([heights[i], i])

        else:
            nse_left_index.append(-1)
            nse_left.append([heights[i], i])

        i += 1

    # calculating the nse right

    j = n - 1

    while j >= 0:

        while nse_right and heights[j] <= nse_right[-1][0]:
            nse_right.pop()

        if nse_right:
            nse_right_index[j] = nse_right[-1][1]
            nse_right.append([heights[j], j])

        else:
            nse_right_index[j] = n
            nse_right.append([heights[j], j])

        j -= 1

    max_area = 0

    for i, (left, right) in enumerate(zip(nse_left_index, nse_right_index)):
        area = ((right - left) - 1) * heights[i]

        max_area = max(max_area, area)

    return max_area


def maximal_rectangle(matrix):
    # convert the matriz to a 1 D array

    height = len(matrix)
    width = len(matrix[0])

    histogram = [0] * width

    max_rectangle = 0

    for i in range(height):

        for j in range(width):

            if matrix[i][j] != "0":
                histogram[j] = histogram[j] + 1
            else:
                histogram[j] = 0

        # calling the histogram_area function on each row
        max_rectangle = max(max_rectangle, histogram_area(histogram))

    return max_rectangle


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
matrix = [["0"]]
print(maximal_rectangle(matrix))
