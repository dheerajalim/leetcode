def two_sum_sorted(numbers, a):
    # using the sorted two sum algo with two pointer approach
    i, j = 0, len(numbers) - 1
    temp = []
    while i < j:
        # this is the tree sum which we want to make it 0
        three_sum = a + numbers[i] + numbers[j]

        # if the sum is >0, then we move the j pointer
        if three_sum > 0:
            j -= 1

        # if we sum is < 0 , then we move the i pointer
        elif three_sum < 0:
            i += 1

        # otherwise we were able to find the triplet that is summing to 0
        else:
            # add this to the result
            temp.append([a, numbers[i], numbers[j]])
            i += 1
            # this case is required that if the numbers[i] == numbers[i-1]
            # this means that for the same number (ith index) we have received the
            # triplet, so we keep on updating the ith index
            while numbers[i] == numbers[i - 1] and i < j:
                i += 1

    return temp


def three_sum(nums):
    # sorting the nums as we will use two sum for sorted nums
    nums = sorted(nums)

    # to store the triplets
    result = []

    # iterate over the input nums
    for i in range(len(nums)):
        # if nums[i] and nums[i-1] are equal that means
        # no need to calculate again for nums[i] as we have already
        # calculated the triplets for nums[i-1](as we need to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        #  else we use the two sum function to get the other two nums
        # which along with cyrrent nums[i] will make a sum of 0
        three_sum_res = two_sum_sorted(nums[i + 1:], nums[i])
        # add all those triplets to the result
        result.extend(three_sum_res)

    return result


nums = [2, 7, 11, 15]
target = 9

# print(two_sum(nums, target))
nums = [-1, 0, 1, 2, -1, -4]
nums = [0, 0, 0]
nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
print(three_sum(nums))
