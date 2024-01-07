"""
Solution is to find the index of NSL and NSR
Then use formula = (Index of NSR - Index NSL) - 1 ; - 1 because same index gets added twice
then height of each element * its maximum width
"""


def area_of_histogram(arr):
    nse_left, nse_right = [], []

    # creating the indexes stack to store the NSE index
    # Notes that nse_right_index is initialized with the
    # index of the histogram at position len(arr) i.e. the
    # non-existing histogram after the last one to get the total width
    nse_left_index, nse_right_index = [], [len(arr)] * (len(arr))
    i = len(arr) - 1
    # iterating from right to left to find NSE on right
    while i >= 0:
        # if the current item is smaller pop from stack
        while nse_right and arr[i] <= nse_right[-1][0]:
            nse_right.pop()
        # Get the index of the NSE on right and
        # update stack with NSE on right details
        if nse_right:
            nse_right_index[i] = nse_right[-1][1]
            nse_right.append((arr[i], i))
        # if the stack is empty ,means the NSE on right is not present
        # hence we pass the last non-existing histogram index as the next smallest
        # this is the len(arr) index
        else:
            nse_right_index[i] = len(arr)
            nse_right.append((arr[i], i))

        i -= 1

    i = 0
    # iterating from left to right to find NSE on left
    while i < len(arr):
        # if the current item is smaller pop from stack
        while nse_left and arr[i] <= nse_left[-1][0]:
            nse_left.pop()

        if nse_left:
            nse_left_index.append(nse_left[-1][1])
            nse_left.append((arr[i], i))
        # if the stack is empty ,means the NSE on left is not present
        # hence we pass the last non-existing histogram index as the next smallest
        # this is the -1 index
        else:
            nse_left_index.append(-1)
            nse_left.append((arr[i], i))

        i += 1

    # calculating the area of each histogram
    # formula = (Index of NSR - Index NSL) - 1 *  height of histogram
    # ; we subtract '1' because same index gets added twice
    result = []

    for i in range(len(arr)):
        result.append(((nse_right_index[i] - nse_left_index[i]) - 1) * arr[i])

    return max(result)


arr = [6, 2, 5, 4, 5, 1, 6]
arr = [2, 1, 5, 6, 2, 3]

print(area_of_histogram(arr))
