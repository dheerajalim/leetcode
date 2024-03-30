'''https://takeuforward.org/data-structure/union-of-two-sorted-arrays/

Time Complexity: O(m+n), Because at max i runs for n times and j runs for m times. When there are no common elements
in arr1 and arr2 and all elements in arr1, arr2 are distinct.

Space Complexity : O(m+n)

'''

# two pointer approach
'''
arr1[] = {1,2,3,4,5,6,7,8,9,10}
arr2[] = {2,3,4,4,5,11,12} 

i = 0 , j = 0

                  i
1,2,3,4,5,6,7,8,9,10

2,3,4,4,5,11,12
           j

if arr[i] < arr[j] and arr[i] != new_arr[-1]: add arr[i] >> i ++

if arr[i] == arr[j] and arr[i] != new_arr[-1]: add arr[i] >> i ++ j++

if arr[i] > arr[j] and arr[j] != new_arr[-1] : add arr[j] >> j ++


'''


def union_sorted_array(arr1, arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:

            if len(result) == 0 or arr1[i] != result[-1]:
                result.append(arr1[i])

            i += 1

        elif arr2[j] < arr1[i]:

            if len(result) == 0 or arr2[j] != result[-1]:
                result.append(arr2[j])

            j += 1

        elif arr1[i] == arr2[j] and arr1[i] != result[-1]:

            if len(result) == 0 or arr1[i] != result[-1]:
                result.append(arr1[i])

            i += 1
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5]
print(union_sorted_array(arr1, arr2))
