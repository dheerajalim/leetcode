"""
https://leetcode.com/problems/subarray-product-less-than-k/description/
"""


def subarray_product(nums, k):
    # since nums is >= 1, so if k <= 1, then we will never
    # get the product , hence we return 0
    if k == 0 or k == 1:
        return 0

    i, j = 0, 0

    n = len(nums)
    # result = [] # this can be used if we want to get the subarrays as well and not just count
    result = 0
    product = nums[j]

    while j < n and i < n:
        # if the product is < k. then we add j-i+1 count to result
        if product < k:
            pos = j - i + 1
            result += pos

            # for x in range(i, i + pos):
            #     subarray = nums[x:j + 1]
            #     result.append(subarray)

            # increment j to next item in nums
            # and update the product
            j += 1
            if j < n:
                product *= nums[j]

        # if the product becomes >= k , then we need to
        # remove the item at ith position from product and increment i
        else:

            product = product // nums[i]
            i += 1

    return result


nums = [1, 2, 3, 4, 5, 6]
k = 725
nums = [1, 2, 3, 4, 5]
k = 1
print(subarray_product(nums, k))


# solution 2: similar logic , better code

def better_solution(nums, k):
    if k == 0 or k == 1:
        return 0

    i, j = 0, 0

    n = len(nums)
    result = 0
    product = 1

    while j < n:
        # get the product
        product *= nums[j]

        # if the product becomes >= k, then we keep on
        # reducing the product and increment i
        while product >= k:
            product //= nums[i]
            i += 1

        # else we just get the total possible subarrays using j-i+1 and increment j
        result += (j - i + 1)
        j += 1

    return result
