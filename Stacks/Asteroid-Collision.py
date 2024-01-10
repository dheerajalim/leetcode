def asteroid_collisioon(arr):
    stack = []

    i = 0
    while i < len(arr):
        # this flag is for condition when the current item
        # itself gets destroyed
        destroy = False
        # this condition checks if the current index is -ve and
        # top of stack is + ve , for collision to work
        while stack and arr[i] < 0 and stack[-1] > 0:
            # we then check the abs value for which asteroid
            # gets destroyed,

            # this is if the top of stack is destroyed
            if abs(arr[i]) > abs(stack[-1]):
                stack.pop()
            # for equal asteroids, both will destroy
            elif abs(arr[i]) == abs(stack[-1]):
                stack.pop()
                # this means the current item is also destroyed
                destroy = True
                break
            else:
                # this means current item is destroyed
                # top of stack is not destroyed
                destroy = True
                break

        # condition to add the item to stack
        if not destroy:
            stack.append(arr[i])

        i += 1

    return stack


arr = [10, 2, -5]
# arr = [8, -8]
# arr = [5, 10, -5]
# arr = [-2,-1,1,2]
arr = [-2, 1, 1, -1]

print(asteroid_collisioon(arr))
