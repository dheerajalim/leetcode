def next_smallest(arr):
    stack = []
    i = len(arr) - 1
    while i >= 0:

        while stack and arr[i] <= stack[-1]:
            stack.pop()

        if stack:
            temp = stack[-1]
            stack.append(arr[i])
            arr[i] = temp
        else:
            stack.append(arr[i])
            arr[i] = -1

        i -= 1

    return arr


arr = [8, 10, 2, 5, 4]
arr = [5, 6, 2, 3, 1, 7]

print(next_smallest(arr))
