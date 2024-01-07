def nearest_smallest_left(arr):
    stack = []

    i = 0

    while i < len(arr):

        while stack and arr[i] <= stack[-1]:
            stack.pop()

        if stack:
            temp = arr[i]
            arr[i] = stack[-1]
            stack.append(temp)

        else:
            stack.append(arr[i])
            arr[i] = -1

        i += 1

    return arr


arr = [4, 5, 2, 10, 8]

print(nearest_smallest_left(arr))
