def twoOutOfThree(nums1, nums2, nums3):

    # first convert each nums to set to avoid duplicate from it then back to list
    # then combine the 3 list
    # get the count of each element, if >= 2, then valid, else ignore

    nums1, nums2, nums3 = list(set(nums1)), list(set(nums2)), list(set(nums3))

    nums = nums1 + nums2 +  nums3
    count_dict = dict()

    for item in nums:
        if count_dict.get(item):
            count_dict[item] += 1

        else:
            count_dict[item] = 1

    # need to check if the count >= 2
    result  = [p[0] for p in list(filter(lambda x : x[1] >= 2, count_dict.items()))]

    return result


nums1 = [1,2,2]
nums2 = [4,3,3]
nums3 = [5]

print(twoOutOfThree(nums1, nums2, nums3))