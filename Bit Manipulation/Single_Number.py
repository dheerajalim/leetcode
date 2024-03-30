def single_number(nums) -> int:
    result = 0
    for i in nums:
        # we keep on Xoring the items
        # if the number appears twice it will become 0
        # leaving the number that appears once as the result
        result = result ^ i

    return result


n = [2, 2, 1, 1, 3]

print(single_number(n))
