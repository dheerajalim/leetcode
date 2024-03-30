def removeDuplicates(nums):

                    # k                 i
    # [0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # [0, 1, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4 ]
    # [0, 1, 2, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # [0, 1, 2, 3, 1, 1, 1, 2, 2, 3, 3, 4]
    # [0, 1, 2, 3, 4, 1, 1, 2, 2, 3, 3, 4]


    if len(nums) == 1:
        return 1

    # if there are more then 1 element, then we will check for unique

    index = 1

    for i in range(0, len(nums)-1):
        if nums[i] == nums[i+1]:
            continue
        else:
            # replace the new element with the repeated one
            nums[index] = nums[i+1]
            index += 1

    return index


nums = [0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums = [1, 1, 2]

removeDuplicates(nums)

print(nums)

# Approach TWO : 2 pointer approach :
# keep i = 0, j =1 initially and then keep on checking nums[j] with nums[i]
# if they are equal then j ++, else nums[i+1] = nums[j] and i ++ , j ++

def removeduplicate_twopointer(nums):
    if len(nums) == 1:
        return 1

    i = 0

    for j in range(1, len(nums)):

        if nums[j] != nums[i]:
            nums[i + 1] = nums[j]
            i += 1

    return i + 1  # as we need to return count of unique elements and i ins index value so we add 1


nums = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4]

print(removeduplicate_twopointer(nums))
print(nums)
