def reverse_array(arr, result_arr):

    if len(arr) == 0:
        return result_arr

    element = arr.pop()
    result_arr.append(element)

    return reverse_array(arr,result_arr)


arr = [10,20,30,40]
print(reverse_array(arr,[]))


def revese_array_index(arr, si, ei):

    if si > ei:
        return arr

    arr[si], arr[ei] = arr[ei], arr[si]

    return revese_array_index(arr,si+1, ei-1)

arr = [10,20,30,40]


print(revese_array_index(arr,0,len(arr)-1))

