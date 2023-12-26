def count_greater_elements(arr):
    stack = []

    i = len(arr) - 1

    while i >= 0:

        if stack and arr[i] <= stack[-1]:

            j = len(stack) - 1
            stack.append(arr[i])

            while j+1 and stack[j] > stack[j+1]:
                stack[j], stack[j+1] = stack[j+1], stack[j]
                j -= 1

            arr[i] = (len(stack) - (j+1)) - 1

        elif stack and arr[i] >= stack[-1]:
            stack.append(arr[i])
            arr[i] = 0

        else:
            stack.append(arr[i])
            arr[i] = 0

        i -= 1
    return arr



arr = [5, 2, 10, 4]
arr = [1, 3, 6, 5, 8, 9, 13, 4]
output = count_greater_elements(arr)
print(output)