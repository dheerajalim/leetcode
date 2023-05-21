'''

Approach 1 : Sort the array and get the last element : sorting is  O(N Log N)
Approach 2 : Keep the variable to store the max value and then keep on comparing the element

'''

def find_largest(arr):

    if len(arr) == 1:
        return arr[0]

    max = arr[0]

    for i in range(len(arr)):

        if max < arr[i]:
            max = arr[i]

    return max


arr = [2,5,1,3,0]

print(find_largest(arr))