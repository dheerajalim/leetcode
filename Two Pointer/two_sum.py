def two_sum(nums, target):
    # hash map to store the number as key and it's index as value
    hash_map = dict()

    # iterate over the give number
    for i, num in enumerate(nums):
        # the required_sum is the sum that we need from the
        # give nums[i] to get the target
        required_sum = target - num

        # if the required sum is already in the hash map
        # we return the answer by returning the index
        if required_sum in hash_map:
            return [hash_map[required_sum], i]

        # else just add the num in the hash map along with its index
        hash_map[num] = i


nums = [3, 3]
target = 6

print(two_sum(nums, target))
