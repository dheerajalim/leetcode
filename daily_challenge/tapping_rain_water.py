def trap(height):

    n = len(height) - 1
    stack_nge_right, right = [], [-1] * len(height)
    stack_nge_left, left = [], []

    nge_left_i = 0

    while nge_left_i <= n:

        while stack_nge_left and height[nge_left_i] > stack_nge_left[-1]:
            stack_nge_left.pop()

        if stack_nge_left:
            left.append(stack_nge_left[-1])
        else:
            left.append(height[nge_left_i])
            stack_nge_left.append(height[nge_left_i])

        nge_left_i += 1

    nge_right_i = n

    while nge_right_i >= 0:

        while stack_nge_right and height[nge_right_i] > stack_nge_right[-1]:
            stack_nge_right.pop()

        if stack_nge_right:
            right[nge_right_i] = stack_nge_right[-1]
        else:
            right[nge_right_i] = height[nge_right_i]
            stack_nge_right.append(height[nge_right_i])

        nge_right_i -= 1

    result = 0
    for i in range(n):
        result += min(left[i], right[i]) - height[i]
    print(left)
    print(right)
    print(result)

height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]

trap(height)