"""
https://www.youtube.com/watch?v=AZOmHuHadxQ

The question says that each element appears twice in the sorted array except one element which appears only once.

So we need to find the element that appears only once, and we can use Binary search for that.

example = [1,1,2,2,3,3,4,5,5,6,6]

Now if we see the array , 4 is the single element and on its right and left we have repeating elements

if the pair is index of
 (even, odd) = this is the left side = > (1,1) is (0,1) index and so on
 (odd, even) = this is the right side => (5,5) is (7,8) index and so on

 Therefore, when we reach a middle element ; we check the following

 if arr[middle-1] != arr[middle] != arr[middle+1] ; then this is the single element
 if arr[middle-1] == arr[middle] != arr[middle+1] ;
 then we need to check if middle is odd then, we move to right
 then we need to check of middle is even then, we move to left

  if arr[middle-1] != arr[middle] == arr[middle+1] ;
 then we need to check if middle is odd then, we move to left
 then we need to check of middle is even then, we move to right


 Also since we need to check middle -1 and middle + 1, hence to avoid out of index error we start with index 1 and
 end index n-1
"""


def find_single_element(arr):

    if len(arr) == 1: # this means only 1 element is presen
        return arr[0]

    if arr[0] != arr[1]:
        return arr[0]

    if arr[len(arr)-1] != arr[len(arr)-2]:
        return arr[len(arr)-1]

    start = 1
    end = len(arr)- 2

    while start <= end:
        middle = (start + end) // 2

        if arr[middle-1] != arr[middle] and arr[middle] != arr[middle+1]:
            return arr[middle]

        # check for (e,o) or (o,e) pairs

        if arr[middle-1] == arr[middle] and arr[middle] != arr[middle+1]:
            if middle % 2 == 0 : # means middle is even and pair is (odd, even)
                end = middle - 1
            else:
                start = middle + 1

        elif arr[middle-1] != arr[middle] and arr[middle] == arr[middle+1]:
            if middle % 2 ==0 : # means middle is even and pair is (even, odd)
                start = middle+ 1
            else:
                end = middle - 1

    return -1


arr = [1,1,2,3,3,4,4,8,8]
arr = [3,3,7,7,10,11,11]
arr = [1,1, 2,2,3,3,4, 5,5,6,6]
print(find_single_element(arr))


