def num_subarray_with_sum(nums, goal):
    n = len(nums)

    i, j = 0, 0

    prefix_sum = 0
    count = 0
    count_zero = 0

    while j < n:

        prefix_sum += nums[j]

        while (prefix_sum > goal or nums[i] == 0) and i < j:

            if nums[i] == 0:
                count_zero += 1
            else:
                count_zero = 0

            prefix_sum -= nums[i]
            i += 1

        if prefix_sum == goal:
            count += 1 + count_zero

        j += 1

    return count


nums = [0, 0, 1, 0, 1]
goal = 1

print(num_subarray_with_sum(nums, goal))
