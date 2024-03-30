

def numberOfPairs(nums):
    # get the count of each number using dictionary
    # then with each value%2. ..if 0 then a pair else leftover

    count_dict = dict()

    for i in nums:

        if count_dict.get(i):
            count_dict[i] += 1
        else:
            count_dict[i] = 1

    answer = [0, 0]
    for key, value in count_dict.items():
        # if value % 2 == 0 : # this makes it a valid pair
        #     answer[0] += value//2 # the no. of pairs
        #
        # else : # this means that the perfect pair does not exists, its an odd number
        extra = value % 2
        value -= extra
        answer[0] += value // 2
        answer[1] += extra

    return answer


pairs = [1, 3, 2, 1, 3, 2, 2]
print(numberOfPairs(pairs))
