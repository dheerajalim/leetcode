# https://leetcode.com/problems/next-greater-element-i/description/
# https://takeuforward.org/data-structure/next-greater-element-using-stack/

"""
Use a stack DS to solve this problem
1. Start from the last element in the given array
2. The NGE of the last element is always -1 as this is the last element
3. Then add this to the top of the stack, the top os stack represents the NGE for the elements in the left of curr position
4. If the cuu position element is < than top of stack , then top of stack is the NGE of the curr pos and add this element as the top of stack
5. If the curr position element is > than top of stack, then pop the stack until the top is > than curr pos else set -1 as the NGE of the curr pos

"""


def next_greater_element(arr: list):
    stack = []
    # the length of the arr
    i = len(arr) - 1
    # starting from the end of arr
    while i >= 0:
        # # if the stack is empty , this means the NGE is not available
        # # Hence push the current element into stack top
        # if not stack:
        #     stack.append(arr[i])
        #     arr[i] = -1
        # # if the stack top is greater than current element
        # # the stack top becomes the NGE for the current element
        # # Update the stack top to current element
        # elif arr[i] < stack[-1]:
        #     temp = arr[i]
        #     arr[i] = stack[-1]
        #     stack.append(temp)
        # # if the current element is greater than stack top
        # # then we pop the stack until it is empty or the top of stack
        # # is greater than the current element
        # else:
        ''' the below code does the same what is commented out on the top , just reduces the steps '''
        while stack and arr[i] >= stack[-1]:
            stack.pop()
        if stack:
            temp = arr[i]
            arr[i] = stack[-1]
            stack.append(temp)
        else:
            stack.append(arr[i])
            arr[i] = -1

        i -= 1

    return arr


arr = [5, 7, 1, 2, 6, 0]
print(next_greater_element(arr))
