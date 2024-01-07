def count_greater_elements(arr):
    stack = []

    i = len(arr) - 1

    while i >= 0:
        # lopping through the array
        # if the stack is not empty
        # and the current element is less than the top of stack
        # That case we need to put this element to the correct position
        if stack and arr[i] <= stack[-1]:
            # we find the length of stack
            j = len(stack) - 1
            # append the new element to the top of stack
            stack.append(arr[i])
            # then keep on swapping the last two elements
            # until the new element reaches the correct position
            while j + 1 and stack[j] > stack[j + 1]:
                stack[j], stack[j + 1] = stack[j + 1], stack[j]
                j -= 1
            # the elements after this position is the count of greater elements
            # We update arr position with the count
            arr[i] = (len(stack) - (j + 1)) - 1
        # if stack is present and the current element is greater
        # than the top of stack that means this is the greatest
        # element already
        elif stack and arr[i] >= stack[-1]:
            stack.append(arr[i])
            arr[i] = 0
        # otherwise kus add the element to the stack
        # and the element has no greater count
        else:
            stack.append(arr[i])
            arr[i] = 0

        i -= 1
    return arr


arr = [5, 2, 10, 4]
arr = [1, 3, 6, 5, 8, 9, 13, 4]
output = count_greater_elements(arr)
print(output)
