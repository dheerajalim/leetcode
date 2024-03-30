

def reverse_array(nums, start, end):

    end = end-1
    while start <= end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

'''Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.'''
def rotate(nums, k):
    # k = 3
    # [1, 2, 3, 4, 5, 6, 7]
    #  0  1  2  3  4  5  6

    n = len(nums)

    # ge the total number of moves we need to do
    if  k == 0:
        return nums

    # if k =7; then rottion makes no sense
    # if k = 9, then totalt rotations are 9 % n (if n=7), then 2 as till 7 rotations it will be same array

    # if the number of rotations is greater than n = len(nums), the  we need k%n as this will be the number of rotations

    if k >= n:
        k = k % n

    # we will first reverse the n-d elements

    reverse_array(nums, 0, n-k)

    reverse_array(nums, n-k, n)

    reverse_array(nums, 0, n)

# Rotating the array to left is also similar approach only the reverse order changes
 # [1,2,3,4,5,6,7] ,k = 3 === [4,5,6,7,1,2,3]

def rotate_left(nums, k):

    n = len(nums)

    if k == 0 or k== n:
        return nums

    if k > n:
        k = nums % k

    reverse_array(nums, 0, k)

    reverse_array(nums,k,n)

    reverse_array(nums, 0, n)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    # rotate right
    rotate(nums,k)
    print(nums)
    nums = [1, 2, 3, 4, 5, 6, 7]

    rotate_left(nums, k)
    print(nums)





