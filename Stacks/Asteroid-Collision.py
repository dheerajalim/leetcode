def asteroid_collisioon(arr):
    stack = []

    i = 0
    while i < len(arr):
        destroy = False
        # while stack and ((arr[i] > 0 and stack[-1] < 0 ) or (arr[i] < 0 and stack[-1] > 0)):
        while stack and arr[i] < 0 and stack[-1] > 0:

            if abs(arr[i]) > abs(stack[-1]):
                stack.pop()
            elif abs(arr[i]) == abs(stack[-1]):
                stack.pop()
                destroy = True
                break
            else:
                destroy = True
                break
        if not destroy:
            stack.append(arr[i])

        i += 1

    return stack

arr = [10, 2 , -5]
# arr = [8, -8]
# arr = [5, 10, -5]
# arr = [-2,-1,1,2]
arr = [-2,1,1,-1]

print(asteroid_collisioon(arr))

