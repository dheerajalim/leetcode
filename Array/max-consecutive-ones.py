'''

https://leetcode.com/problems/max-consecutive-ones/

Time Complexity: O(N) since the solution involves only a single pass.

Space Complexity: O(1) because no extra space is used.

'''

def findMaxConsecutiveOnes(nums):

    # keep a count variable >> ++count if 1 is seen, else reset count = 0
    # maintain a max_count which will get compared with the count

    max_count, count = 0, 0

    for i in nums:

        if i == 1 :
            count += 1
            if count > max_count:
                max_count = count
        else:

            count = 0

    return max_count


nums = [1,1,0,1,1,1]
nums = [1, 0, 1, 1, 0, 1]
print(findMaxConsecutiveOnes(nums))




