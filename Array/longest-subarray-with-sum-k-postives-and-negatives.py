'''

We will store the sum in a hash map, any time we get sum > k, we check in the hash map if we have sum-k present
in the hashmap , if yes then we calculate the length , if length  > current length thn update

https://takeuforward.org/arrays/longest-subarray-with-sum-k-postives-and-negatives/
'''

def longest_subarray(arr,k):

    hashmap = dict()

    subarray_length = 0

    subarray_sum = 0

    i = 0
    n = len(arr)

    for i in range(n):

        subarray_sum += arr[i]

        if subarray_sum == k:
            subarray_length = max(subarray_length, i+1)

        rem = subarray_sum - k

        if rem in hashmap:
            subarray_length = max(subarray_length, i - hashmap[rem])

        if subarray_sum not in hashmap:
            hashmap[subarray_sum] = i

    return subarray_length


arr = [-1, 1, 1,-1,1]
k = 1

print(longest_subarray(arr,k))