'''

https://takeuforward.org/arrays/find-the-missing-number-in-an-array/

1 . Take the sum of 1 to N integers using n(n-1)/2
2. Take the sum of the array
3. The difference of step 1 and step 2 is the missing integer

Time Complexity: O(N), where N = size of array+1.
Reason: Here, we need only 1 loop to get the sum of the array elements. The loop runs for approx. N times. So, the time complexity is O(N).

Space Complexity: O(1) as we are not using any extra space.

'''


def missing_num_array(arr,n):

    # sum of the arr
    arr_sum = sum(arr)

    # 1 to n integer sum
    integer_sum = n*(n+1)/2

    return int(integer_sum - arr_sum)



arr  =[1,2,4,5]
n = 5

arr = [1,3]
n = 3

print(missing_num_array(arr,n))