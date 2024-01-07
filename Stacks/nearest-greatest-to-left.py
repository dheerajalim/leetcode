def nearest_greatest_left(arr):
    stack = []
    i = 0
    while i < len(arr):

        while stack and arr[i] >= stack[-1]:
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


arr = [1, 3, 2, 4]

print(nearest_greatest_left(arr))
