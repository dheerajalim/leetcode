"""

    Consecutive smaller or equal to it on the left  ==== >

    If we find the NGL index and then  = [current index - NGL index]  = Solution)

    Store the Pair in stack [NGL, index]
"""


def stock_span(arr):
    stack = []  # to store the element and its index
    stack_indexes = []  # to store NGE index

    i = 0
    # since we need to find from left, hence loop starts from 0
    while i < len(arr):
        # if the current element is greater than top of stack
        # then keep on popping
        while stack and arr[i] >= stack[-1][0]:
            stack.pop()

        if stack:
            # the top of stack contains pair of NGE and its index
            # fetch the index of NGE
            nge_index = stack[-1][1]

            # Updating the stack_indexes list with NGE index
            stack_indexes.append(nge_index)
            # updating the stack with current element and its index
            stack.append((arr[i], i))

        else:
            # if the stack is empty , then we simply add
            # item and its index
            # and stack_indexes store -1 as NGE does not exist
            stack.append((arr[i], i))
            stack_indexes.append(-1)

        i += 1

    stock_span = []
    for i in range(len(arr)):
        stock_span.append(i - stack_indexes[i])

    return stock_span


arr = [100, 80, 60, 70, 60, 75, 85]
print(stock_span(arr))
