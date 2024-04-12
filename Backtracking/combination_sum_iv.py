"""NEED TO CHECK WHEN Dynamic programming is started"""
def backtracking(nums, target, curr, result,mem):
    if sum(curr) == target:
        # result.append(curr.copy())
        # print(result)
        return 1
    # print(mem)
    if mem[0][sum(curr)] != -1:
        return mem[0][sum(curr)]
    for i in range(len(nums)):

        if curr and sum(curr) + nums[i] > target:
            break

        curr.append(nums[i])

        temp = backtracking(nums, target, curr, result, mem)
        result[0] += temp
        curr.pop()

    mem[0][sum(curr)] = result[0]
    return 0

def combination_sum(nums, target):
    result = [0]
    curr = []
    # to help reduce the iterations when sum exceeds target
    nums = sorted(nums)
    mem = [[-1 for _ in range(201)] for _ in range(1001)]
    backtracking(nums, target, curr, result, mem)

    return result[0]


nums = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
target = 10

print(combination_sum(nums, target))
