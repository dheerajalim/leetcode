def contains_duplicate(nums, k):
    if k == 0:
        return False

    i, j = 0, 0
    n = len(nums)
    # to store the num that we have crossed
    # already in the k size window
    occur_nums = set()

    # iterate until the last element
    while j < n:

        # of the abs diff of j - i <= k
        # this means we are in limits of window size
        # if we see an element at position  j already in set
        # then we return true, else add iten at j in set
        if abs(j - i) <= k:

            if nums[j] in occur_nums:
                return True
            else:
                occur_nums.add(nums[j])
                j += 1

        # else now we need to shrink the window size
        # as abs (j-i) > k, so we move i by 1  to right
        # also we remove the num at position i from set
        # as this has moved out from the window now
        else:
            occur_nums.remove(nums[i])
            i += 1

    # at the end after iteration , since we did not
    # get duplicate we return False
    return False


nums = [1, 2, 3, 1, 2, 3]
k = 2

print(contains_duplicate(nums, k))
