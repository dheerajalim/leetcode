'''

https://takeuforward.org/data-structure/longest-subarray-with-given-sum-k/

TWO pointer approach

THIS CAN ALSO BE SOLVED USING HASHING APPROACH, BUT THAT IS BETTER APPROACH AND WILL BE USED IN CASE THE ARRAY
HAS NEGATIVE NUMBERS
'''

def longest_subarray(arr, k):

    n = len(arr)

    len_subarray = 0

    left, right = 0, 0

    subarray_sum = arr[0]

    while right < n:

        while left <= right and subarray_sum > k:
            subarray_sum -= arr[left]
            left += 1

        if subarray_sum == k:
            len_subarray = max(len_subarray, right - left +1)

        right += 1

        if right < n:
            subarray_sum += arr[right]

    return len_subarray


arr = [1,2,3,5,9]
k = 10

print(longest_subarray(arr,k))


