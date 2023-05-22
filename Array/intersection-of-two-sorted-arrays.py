'''
https://takeuforward.org/data-structure/intersection-of-two-sorted-arrays/

Time Complexity: O(n) { Since the elements are compared within the single pass for both the arrays this approach would take a linear time and in the worst case O(n1+n2) where n1 = A.size() and n2 = B.size() }.

Space Complexity: O(1) { There is no extra space used in the two-pointers approach }.

'''

# two pointer approach

'''
A: [1 2 3 3 4 5 6]
 B: [3 3 5]
 
 i
 1 2 3 3 4 5 6
 3 3 5
 j
 
 if a[i] == b[j] : then i++ j++
 if a[i] != b[j] :
    if a[i] < b[j]:
        i += 1
    else:
        j += 1
'''


def intersection_sorted_array(arr1, arr2):
    i, j = 0, 0
    result = []
    while i < len(arr1) and j < len(arr2):

        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1
            j += 1

        else:
            if arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1

    return result


arr1 = [1, 2, 3, 3, 4, 5, 6]
arr2 = [3, 3, 5]

arr1 =  [1, 2, 3, 3, 4, 5, 6]
arr2 =  [3, 5]

print(intersection_sorted_array(arr1, arr2))