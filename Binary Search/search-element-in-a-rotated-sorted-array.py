"""

https://takeuforward.org/data-structure/search-element-in-a-rotated-sorted-array/

https://leetcode.com/problems/search-in-rotated-sorted-array/

The idea is to apply Binary Search, but we can't do that directly as the array is rotated and sorted., hence we need to
find a different way

1. Find the start and end of the array
2. Calculate the middle of the array while start <= end
3. If the arr[middle] == target , then we have the answer
4. Else we check if the arr[start] < arr[middle], this means that the left part from middle is sorted
    Note: AT once either left can be sorted or right
    > Now we know that the left part is sorted, we next can check that if  arr[low] <= target <= arr[middle]
    > this means the left part is where we need to look for target, hence we update end = midle -1
    > else we move to left side; hence start = middle+ 1

5. Else , if step 4 is not valid then the right part is sorted
    > if  arr[middle] <= target <= arr[end]; this means right part is where we need to search
    > update the start = middle + 1
    > else we move to right side ; hence end = middle- 1
"""


def search_element(arr, target):

    start = 0
    end = len(arr) - 1

    while start <= end:

        middle = (start + end) //2

        if arr[middle] == target:
            return middle

        if arr[start] <= arr[middle]:

            if arr[start] <= target <= arr[middle]:
                end = middle-1
            else:
                start = middle + 1

        else:
            if arr[middle] <= target <= arr[end]:
                start = middle + 1
            else:
                end = middle- 1


    return -1


arr = [4,5,6,7,0,1,2,3]
target = 0
arr = [4,5,6,7,0,1,2]
target = 3

arr = [1,3]
target = 3

print(search_element(arr,target))