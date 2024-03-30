
'''
https://leetcode.com/problems/single-number/

'''
def singleNumber(nums):
    '''
    Approach 1 :

    We tak dictioanry and get the count of each element
    The element whose count is 1, is the answer

    This will take O(M Log N) as we will insert in dict where M = size of the map i.e. M = (N/2)+1. N = size of the array.

    Appraoch 2 (Optimal) using XOR
    > XOR of same numbers is always 0
    hence xor of all number sin list will be the number which appears alone as xor of number and 0 is number
    '''

    xor = 0
    for i in nums:

        xor ^= i

    return xor


nums = [2,2,1]
nums = [4,1,2,1,2]
print(singleNumber(nums))


