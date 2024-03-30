def min_sub_array(nums, target):
    i, j = 0, 0
    n = len(nums)

    min_len = float('inf')
    window_sum = 0
    while j < n:
        # keep on adding the values that we are adding to the window
        window_sum += nums[j]
        # if the window sum becomes >= target
        # then this is the length we need
        while window_sum >= target:
            temp_len = j - i + 1
            # as we need to minimize the length of the window
            min_len = min(min_len, temp_len)
            # now we need to slide the window from i to i+1
            # as we have found window >= target,
            # we reduce the window sum as we  are trying to minimize the length
            # hence we move i t i+1 and subtract value at ith index from window_size
            # until we satisfy the condition  window_sum >= target
            window_sum -= nums[i]
            i += 1

        # else we keep on increasing the window size looking for
        # sum >= target
        j += 1

    return min_len if min_len != float('inf') else 0


target = 11
nums = [1, 1, 1, 1, 1, 1, 1, 1]

print(min_sub_array(nums, target))
