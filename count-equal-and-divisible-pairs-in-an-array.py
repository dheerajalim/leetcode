def countPairs(nums, k):
    # using hashing to get all the pairs

    # [0, 1][0, 2][0, 3][0, 4]
    # [1, 2][1, 3][1, 4]
    # [2, 3][2, 4]
    # [3, 4]

    count_dict = dict()
    result_count = 0
    for item in range(len(nums)):

        if count_dict.get(nums[item]):
            count_dict[nums[item]].append(item)
        else:
            count_dict[nums[item]]= [item]

    for v in count_dict.values():
        if len(v) == 2:

            if (v[0] * v[1]) % k == 0:
                result_count += 1
        else:
            for i in range(len(v)):
                for j in range(i+1,len(v)):
                    result_count += 1 if (v[i] * v[j]) % k == 0 else 0

    return (result_count)




nums = [1,2,3,4]
k =1
print(countPairs(nums,k))