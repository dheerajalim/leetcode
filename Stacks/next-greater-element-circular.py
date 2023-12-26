# the same version as Next Greater Element
# but for a circular array

def next_greater_element(arr: list):
    stack = []
    # the length of the arr
    n = len(arr)
    i = (2 * len(arr)) - 1
    # starting from the end of arr
    while i >= 0:
        x = i % n
        while stack and arr[i % n] >= stack[-1]:
            stack.pop()
        # here we assume that we only will action if the index is of actual array length
        if i < n:
            if stack:
                temp = arr[i]
                arr[i] = stack[-1]
                stack.append(temp)
            else:
                stack.append(arr[i])
                arr[i] = -1
        else: # this condition is to update the NGE of the new assumed array copy
            stack.append(arr[i % n])

        i -= 1

    return arr


arr = [5, 7, 1, 2, 6, 0]
print(next_greater_element(arr))
